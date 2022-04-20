import sys
import os.path
import smtplib
import random
import string
import nameslist
from getpass import getpass


def get_email_list():
    email_list = []
    for i in range(10):
        random_numbers = random.randint(1, 10)
        random_server_sel = "@" + random.choice(email_providers) + random.choice(tlds)
        randnames = random.choice(nameslist.Names)
        random_2lettercomb = ''.join(random.choice(string.ascii_letters) for l in range(1))
        email_list.append(randnames + random_2lettercomb + str(random_numbers) + random_server_sel)
    return email_list



if len(sys.argv) <= 2:

    print('Parameter:')
    print('  mailfrom: pythontest0606@gmail.com')
    print('  rcptto:   elcinuyanik@hotmail.com')
    print('  emlfile:  Message file in eml format. When emlfile is not specified, an empty message will be send.')

    print('Example:')
    print('  $ python ' + sys.argv[0] + ' mailfrom rcptto emlfile')
    sys.exit(0)

server = 'smtp.gmail.com'
port = 587
mailfrom = sys.argv[1]
rcptto = sys.argv[2]

message = ''
if len(sys.argv) >= 4:
    filename = sys.argv[3]
    if not os.path.isfile(filename):
        print('File "' + filename + '" not found.')
        sys.exit(0)
    with open(filename) as f:
        message = f.read()

smtp = None

try:
    smtp = smtplib.SMTP(server, port)
    smtp.starttls()
    password = getpass()
    smtp.login(mailfrom,password)
    smtp.sendmail(mailfrom, rcptto, message)
except Exception as e:
    print('Failed to send mail.')
    print(str(e))
else:
    print('Succeeded to send mail.')
finally:
    if smtp != None:
        smtp.close()


email_providers = ["yahoo","gmail","hotmail","outlook"]
tlds = [".com",".co.uk",".net",".au",".org"]

print(get_email_list())




