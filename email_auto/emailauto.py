import smtplib
import os

myemail = 'yfzhang819@gmail.com'
#os.environ.get('DB_USER')
mypassword = 'htyhtcwhgkehfgmj'
#os.environ.get('DB_PASS')

#est conn w gmail
with smtplib.SMTP('smpt.gmail.com', 587) as smtp:
    #identify w mail server as encrypted connection
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(myemail, mypassword)

    #email template 
    subject = 'This is the subject'
    body = 'This is body'

    # format plain txt email
    msg = f'Subject: {subject} \n\n{body}'

    #smtp.sendmail(SENDER, RECIEVR, msg)
    smtp.sendmail(myemail, 'yfzhang819@gmail.com', msg)

    smtp.quit()
'''
# reading the spreadsheet
email_list = pd.read_excel('C:/Users/user/Desktop/emails.xlsx')
  
# getting the names and the emails
names = email_list['NAME']
emails = email_list['EMAIL']
  
# iterate through the records
for i in range(len(emails)):
  
    # for every record get the name and the email addresses
    name = names[i]
    email = emails[i]
  
    # the message to be emailed
'''