from SimpleTelnetMail import TelnetMail

client = TelnetMail("192.168.10.225", port=25, from_ = "elcin@dbx.local", to = ["elcin@dfxtest.local"], message = "Secret and secure email with Telnet.")
client.send_mail()