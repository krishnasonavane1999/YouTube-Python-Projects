# send mails using python 📩

import smtplib
# simple mail transfer protocol

my_mail = "<your mail id here>"
passcode = "<your generted password here?"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls() # transfer layer security
connection.login(user=my_mail, password=passcode)


# mail_content = "Subject: Trip on this weekned? \n\n Hey Buddy, how are you? Iss weekned pe Goa plan kare?"

try:
    connection.sendmail(from_addr=my_mail, to_addrs="krishna@yopmail.com", msg=mail_content)
except Exception as e:
    print("Something went wrong while sending the mail", e)
    
connection.close()



