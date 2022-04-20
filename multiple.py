import os.path
import smtplib
import random
import string
import nameslist
from getpass import getpass
import usermail


def get_email_list():
    dummy_list = []
    email_providers = ["yahoo", "gmail", "hotmail", "outlook"]
    tlds = [".com", ".co.uk", ".net", ".au", ".org"]
    real_list = random.sample(usermail.Users, random.randint(1, 4))
    real_listlen = len(real_list)
    for i in range(random.randint(totalRcpt - real_listlen, totalRcpt - real_listlen)):
        random_numbers = random.randint(1, 10)
        random_server_sel = "@" + random.choice(email_providers) + random.choice(tlds)
        dummy = random.choice(nameslist.Names)
        random_2lettercomb = ''.join(random.choice(string.ascii_letters) for x in range(5))
        dummy_list.append(dummy + random_2lettercomb + str(random_numbers) + random_server_sel)
    print("Gönderilecek Gerçek Mail Adresleri: " + str(real_list))
    print("Gönderilecek Dummy Mail Adresleri: " + str(dummy_list))
    all_mail_list = real_list + dummy_list
    return all_mail_list


totalRcpt = int(input("Gönderilecek Mail Adedi Girin: "))
server = 'smtp.gmail.com'
port = int('587')
mailfrom = 'pythontest0606@gmail.com'
password = getpass(mailfrom + " Adresinin Şifresini Girin: ")
emlfile = random.choice(os.listdir("/home/elcin/PycharmProjects/generate/emlfiles"))
print("Gönderilecek eml Dosyası: " + emlfile)
try:
    smtp = smtplib.SMTP(server, port)
    smtp.starttls()
    smtp.login(mailfrom, password)
    rcpt = get_email_list()
    smtp.sendmail(mailfrom, rcpt, emlfile)
except Exception as e:
    print('Failed to send mail.')
    print(str(e))
else:
    print('Succeeded to send mail.')
