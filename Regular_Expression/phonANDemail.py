#! python 3
# phoneANDemail.py - Finds phone numbers and email addresses on the clipboard

import pyperclip, re

#create phone regex
phone_regex = re.compile(r'''(
(\d{3}|\(\d{3}\))?    #areacode
(\s|-|\.)?           #seperator
(\d{3})              #frst 3 digits
(\s|-|\.)           #seperator
(\d{4})             #last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension
)''',re.VERBOSE)

#create email regex
email_regex = re.compile(r'''(
[a-zA-Z0-9._%+-]+      #username
@                      # @ symbol
[a-zA-Z0-9.-]+         # domain name
(\.[a-zA-Z]{2,4})      # dot-something

)''',re.VERBOSE)

#find matches in the text
text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phoneNUM = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNUM += ' x' + groups[8]
    matches.append(phoneNUM)
for groups in email_regex.findall(text):
    matches.append(groups[0])

#copy results to clip board
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard!!!')
    print('\n'.join(matches))
else:
    print('No phone no.s or email found!!!')