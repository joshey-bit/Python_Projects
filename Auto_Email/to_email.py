#program to list the 'to' email ids, from the matched data of email finder

from email_finder import matches

#function to choose emails to send message:
def to_email_id():
	print('do you want to start new or update and send?')
	response = input('enter 0 to start_new <or> 1 to update: ')
	if response == '0':
		try:
			with open('email_list.txt') as fb:
				emails = fb.read()
		except (FileNotFoundError):
			if matches:
				with open('email_list.txt','a') as fb:
					fb.write(', '.join(matches))
				with open('email_list.txt') as fb:
					emails = fb.read()

	elif response == '1':
		with open('email_list.txt','a') as fb:
			fb.write(', ')
			fb.write(', '.join(matches))
		with open('email_list.txt') as fb:
			emails = fb.read()


	return emails


# print(to_email_id())