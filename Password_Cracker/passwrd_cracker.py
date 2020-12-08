#program to crack passwords
from random import randint

#the charter list for guessing
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
'u','v','w','x','y','z']

password = input('Enter your password: ')

#initialize an empty guess variable
guess = ''

while (guess != password):
	guess = ''
	
	for char in range(len(password)):
		guess_letter = str(characters[randint(0, 25)])
		guess = guess + guess_letter

	print(guess)

#when guess is same as password, while loop breaks 
print('\nyour password is: '+ str(guess))

