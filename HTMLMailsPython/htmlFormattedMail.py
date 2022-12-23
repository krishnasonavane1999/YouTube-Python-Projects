# Send Beautiful HTRML formatted mails with some attachments(.pdf, images, etc)
import smtplib
from email.message import EmailMessage

my_mail = "<your mail here>"
passcode = "<your password here>"
recipient = "recipient's mail address"

mail_content = EmailMessage()

# Mail metadata
mail_content['Subject'] = "Some Inspiration Programming Quotes!"
mail_content['From'] = my_mail
mail_content['To'] = recipient

# Prepare HTMl Formatted Mail
mail_content.set_content('''<!DOCTYPE html>
<html>
    <body>
        <div style="background-color:#97a3b8;padding:10px 20px;">
            <h2 style="font-family:'Calibri'; text-align:center">Hello World</h2>
        </div>
        <div style="padding:50px 0px">
            <div style="text-align:center">
                <img src="https://images.pexels.com/photos/2764993/pexels-photo-2764993.jpeg?auto=compress&cs=tinysrgb&w=1600&lazy=load" style="height: 400px; width:400px al">
                <div style="text-align:center;">
                    <h3>Thoughts</h3>
                    <h4 style="font-family:calibri">Truth can only be found in one place: the code.” ― Robert C. Martin, </h4>
                    <a href="https://www.goodreads.com/quotes/tag/programming">Click here to read More</a>
                </div>
            </div>
        </div>
    </body>
</html>''', subtype='html')

# Add attachments as well
with open("coding.jpg", "rb") as attahment:
    mail_content.add_attachment(attahment.read(), maintype="application", subtype="octet-stream", filename=attahment.name)


with smtplib.SMTP_SSL('smtp.gmail.com') as mail_account:
    mail_account.login(user=my_mail, password=passcode)
    mail_account.send_message(mail_content)

