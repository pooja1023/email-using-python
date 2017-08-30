import smtplib
#content='hello this is a simple email sending through pyhton'
message = """From:sender name <sender mail id>
To:receiver name <receiver mail id>
Subject: Email using python.

I sent you this message using python.
"""


mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login('sender mail id','password')
mail.sendmail('sender mail id','receiver mail id',message)
mail.close()


