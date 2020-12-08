# A program to create virtual assistant(Aarya) to automate tasks
import os
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import random
import requests
import webbrowser
import json
import smtplib
from webbrowser import Mozilla


# creating an engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[5].id) #the voices[int].id gives the name of voices= in this case its zira_11.0
engine.setProperty('voice', voices[3].id)

#know the rate of voice (speed)
rate = engine.getProperty('rate')
# print(rate)
engine.setProperty('rate',145)

#to make mozilla as default browser
webbrowser.register('firefox', Mozilla('mozilla'))

#calling personal email details from json file
with open('email_details.json') as file_object:
	data = json.load(file_object)

#store the data as respective files
sender_emailID = data['email_id']
passkey = data['password']


# create function to speak
def speak(text):
	engine.say(text)
	engine.runAndWait()


# create function to wish me
def wish_me():
	hour = int(datetime.datetime.now().hour)
	if hour >= 0 and hour < 12:
		speak("Good morning!")
	elif hour >= 12 and hour < 18:
		speak("Good afternoon!")
	else:
		speak("Good Evening")

	speak("I am Aarya, How may i help You?")

# create function to take commands from user
def take_command():
	'''
	it takes microphone input from the user and returns string output
	'''
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening.......")
		r.pause_threshold = 1
		r.energy_threshold = 300
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio,language='en-in')
		print(f'User said: {query}')
	except Exception as e:
		print(e)
		print("Pardon, say that again please...")
		return "None"

	return query

#a function for softwares in locations directory
def software(query):
	global soft_directory
	soft_directory = 'locations/'
	programs = os.listdir(soft_directory) 
	# print(programs)

	#dictionary of programs in soft-directory
	soft_dictionary = {
		'app_name_key': 'application shortcut link'
	}
	'''
	e.g.: soft_dictionary = {
		'paint': 'ms paint shorcut link'
	}
	'''

	#check for query in dictionary
	if query in soft_dictionary.keys():
		return soft_dictionary[query]
	else:
		return None

#function to create dictionary of contacts id according to their name
def contacts(name):
	contact_dictionary = {
	        'reciver_name': 'reciever email id'
	}

	#check if name exsists in contacts dictionary
	if name in contact_dictionary.keys():
		return contact_dictionary[name]
	else:
		return None

#a function to send Email
def sendEmail(to, content):
	'''this uses smtp library to send email via gmail'''
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login(sender_emailID, passkey)
	server.sendmail(sender_emailID, to, content)
	server.close()

#function to play videos on youtube
def playonyoutube(topic):
    """Will play recent video on following topic"""
    url = 'https://www.youtube.com/results?q=' + topic
    # print(url)
    count = 0
    cont = requests.get(url)
    # print(cont)
    data = cont.content
    # print(data)
    data = str(data)
    lst = data.split('"')
    for i in lst:
        count+=1
        if i == 'WEB_PAGE_TYPE_WATCH':
            break
    if lst[count-5] == "/results":
        raise Exception("No video found.")
    
    #print("Videos found, opening most recent video")
    webbrowser.open("https://www.youtube.com"+lst[count-5])
    
    return "https://www.youtube.com"+lst[count-5]	


'''
|||||||||||||||||||||||||||||||||||-------Program Run Enviroment------|||||||||||||||||||||||||||||||||||||||
'''

# excuting main function for particular tasks
if __name__ == '__main__':

	wish_me()
	while True:
		query = take_command().lower()


		# saying thank you terminates the while loop
		if ('thank you' in query) or ("it's ok" in query):
			if "it's ok" in query:
				speak('i am still learning, thank you for feedback')
				break
			else:
				speak('you are welcome!')
				break

		#logic to execute task based on query
		# to search wikipedia
		elif 'wikipedia' in query:
			speak('Searching wikipedia..')
			query = query.replace('wikipedia', '')
			results = wikipedia.summary(query, sentences=1)
			speak("According to wikipedia....")
			# print(results)
			speak(results)

		# to open in browser
		elif ('open youtube' in query) or ('open google' in query) or ('open moneycontrol' in query) or ('open amazon' in query):
			var = query.replace('open ', '')
			# print(var)
			speak(f'opening {var}')
			webbrowser.open('www.'+ var +'.com')

		#to search in browser
		elif 'google search' in query:
			speak('what to search?')
			while True:
				query = take_command().lower()
				if query != 'none':
					link = f'https://www.google.com/search?q={query}'
					webbrowser.open(link)
					break
				else:
					speak('be clear..')	 

		#to play videos in youtube
		elif 'play youtube' in query:
			speak('what to play?')
			while True:
				query = take_command().lower()
				if query != 'none':
					playonyoutube(query)
					break
				else:
					speak('be clear!!')



		#to enquire present time
		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M")
			speak(f'the time is {strTime}')
		

		# to open system programs
		elif 'play music' in query:
			music_dir = 'Audio/'
			songs = os.listdir(music_dir)
			# print(songs)
			song_number = random.randint(0, (len(songs)-1))
			# print(song_number)
			os.startfile(os.path.join(music_dir,songs[song_number]))

		elif 'open software' in query:
			#ask for software
			speak('which software do you like to open?')
			query = take_command().lower()
			# checks wheter query is in software function and returns respective link if exist otherwise returns none
			result = software(query)
			if result:
				os.startfile(os.path.join(soft_directory,result))
			else:
				speak('no software by that name, please check')


		#to send Email to someone
		elif 'send email' in query:
			#ask name of To person
			speak('please specify name of reciever..')
			name = take_command().lower()
			#check for name in contacts
			email_id = contacts(name)

			# print(email_id)

			#email_id exists in contacts send mail other wise no
			if email_id:
				try:
					speak('what should I say?')
					content = take_command()
					to = email_id
					sendEmail(to, content)
					speak('Email sent successfully')
				except Exception as e:
					print(e)
					speak('sorry couldnot send email..')

			else:
				speak(f'{name} doesnot exist in contacts')

