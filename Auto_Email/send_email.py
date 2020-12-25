#Program to send email to all the email ids that were found by the email finder
import smtplib, json, os, imghdr
from email.message import EmailMessage
from to_email import to_email_id


#calling personal email details from json file
with open('email_details.json') as file_object:
	data = json.load(file_object)

#store the data as respective files
sender_emailID = data['email_id']
passkey = data['password']

#calling message_body to load body:
with open('message_body.txt') as content:
	body = content.read()

#to email address from to_email module
email_id = to_email_id()

#a function to send Email
def sendEmail(msg):
	'''this uses smtp library to send email via gmail'''
	with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
		server.login(sender_emailID, passkey)
		server.send_message(msg)
		server.close() 

#message:
msg = EmailMessage()
msg['Subject'] = 'Job Application'
msg.set_content(body)
msg['From'] = sender_emailID
msg['To'] = email_id

print(msg['To'])


#add attachment(eg.: Resume)
#call the resume file from directory
directory = 'resume/'
resume = os.listdir(directory)
resume = ''.join(resume)
# print(resume)

resume_location = directory+resume

with open(resume_location,'rb') as cv:
	file_data = cv.read()
	file_name = (cv.name).replace('resume/', '')

#addign resume to message 
msg.add_attachment(file_data, maintype='image', subtype= 'octet-stream', filename= file_name)


#to send email:
try:
	sendEmail(msg)
	print('email sent succesfully')
except (Exception) as e:
	print('sending failed..........')
	print(e)
	