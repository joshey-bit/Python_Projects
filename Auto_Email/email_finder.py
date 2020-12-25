#! python 3
# email_finder.py - Finds email addresses copied on the clipboard

import pyperclip, re
#create email regex
email_regex = re.compile(r'''(
[a-zA-Z0-9._%+-]+      #username
@                      # @ symbol
[a-zA-Z0-9.-]+         # domain name
(\.[a-zA-Z]{2,4})      # dot-something

)''',re.VERBOSE)

#to find email matches in the copied text
text = str(pyperclip.paste())
matches = []

for groups in email_regex.findall(text):
    matches.append(groups[0])


#copy results to clip board
if len(matches) > 0:
    print('Email ID sorted......')
    # print('\n'.join(matches))
    # print(matches)
else:
    print('No phone no.s or email found!!!')