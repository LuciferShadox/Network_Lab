#  Python implementation

# 	Program    :  Simple Mail Transfer Protocol
# 	Status     :  Stable
# 	Created by :  Sarath Peter

## Import packages here

import smtplib
import getpass

## Write functions here

## Write code here

server = smtplib.SMTP('smtp.gmail.com', 587) ## setting gmail SMTP
server.starttls()   # starting tls service
print("------ Server is online ------")

## Authentication Data
username = raw_input(" Enter Username : ")
password = getpass.getpass(" Enter Password : ") ## To type passwords as hidden

try:
    server.login(username, password) ## Login Attempt

except smtplib.SMTPAuthenticationError:
    print("==(!)== Sign in error ==(!)==") ## Login Failed

else:
    print("\nWelcome "+username[:9]) ## Greeting
    target = raw_input("\n Enter target mail address : ") ## Mail Address to send test mail
    test = "Subject: Auto generated mail \n\n The following is a generated mail sent from "+username+". \nPlease do not reply \n\n Regards\n Sarath Peter"
    server.sendmail(username,target,test) ## Sending mail to give target mail address
    print("\n---- Test Mail Send to "+target+" ----")
    server.close() ## Closing connections
