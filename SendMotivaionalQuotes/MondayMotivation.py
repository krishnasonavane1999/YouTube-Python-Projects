# Monday Motivation 🔥
import smtplib
from email.message import EmailMessage
import datetime as dt
import random
import os

# TODO: set metatadata
my_mail = "<sender's mail address>"
passcode = "<your password here>"
recipients = ["receiver's mail1", "receiver's mail2", etc]

# TODO: get random quote from the file
def getRandomQuote():
    with open(os.getcwd() + "/quotes.txt") as data:
        all_quotes = data.readlines()
        return random.choice(all_quotes)

# TODO: Set mail content
def getMailContent(quote):
    return '''<!DOCTYPE html>
<html>
    <body>
        <h1 style="font-family:'Calibri'; text-align:center">Let's Get that thing Done 😎</h1>
        <div style="padding:20px">
            <div style="text-align:center">
                <img src="https://images.pexels.com/photos/3831849/pexels-photo-3831849.jpeg?auto=compress&cs=tinysrgb&w=1600&lazy=load" style="height: 500px; width:400px">
                <div style="text-align:center;">
                    <h2 style="font-family:calibri">{quote}</h2>
                </div>
            </div>
        </div>
    </body>
</html>'''.format(quote=quote)

# TODO: prepare and send mail

mail_content = EmailMessage()

mail_content['Subject'] = "Monday Motivation! 🔥"
mail_content['From'] = my_mail
mail_content['To'] = recipients

mail_content.set_content(getMailContent(getRandomQuote()), subtype='html')

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

today = weekdays[dt.datetime.now().weekday()]

if today == "Saturday":
    print("So, today is {today} so sending the mail".format(today=today))
    with smtplib.SMTP_SSL('smtp.gmail.com') as mail_account:
        mail_account.login(user=my_mail, password=passcode)
        mail_account.send_message(mail_content)

