#  Python implementation

# 	Program    :  Simple Mail Transfer Protocol
# 	Status     :   Developing
# 	Created by :  Sarath Peter

## Import packages here

import smtplib
import getpass

## Write functions here

## Write code here

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
print("------ Server is online ------")
server.ehlo()

username = raw_input(" Enter Username : ")
password = getpass.getpass(" Enter Password : ")

try:
    server.login(username, password)

except smtplib.SMTPAuthenticationError:
    print("==(!)== Sign in error ==(!)==")

else:
    print("\nWelcome "+username[:9])
    target = raw_input("\n Enter target mail address : ")
    test = "Subject: Auto generated mail \n\n The following is a generated mail sent from "+username+". \nPlease do not reply \n\n Regards\n Sarath Peter"
    server.sendmail(username,target,test)
    print("\n---- Test Mail Send to "+target+" ----")
    server.close()
