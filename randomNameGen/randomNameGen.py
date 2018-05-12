#! python 3

# Script to generate random first and last names
# Make a script to produce a working dictionary
# Can be improved to remove input from user and just randomly generate
	
#------------------------------------------------------
import random

randomNum = random.randint(0,9)

print('Hello! Enjoy your new random name!')

# Display first name
firstName = {'0': 'John', '1': 'Jake', '2': 'Josh', '3': 'Joe', '4': 			'Abbey','5': 'Lenny', '6': 'Osagie', '7': 'Ron', '8': 'Mark', 			'9': 'Raul'}

print(randomNum)
	

# Display last name
lastName = {'0': 'Smith','1': 'Maller', '2': 'Miller', '3': 'Poblobski', 			'4': 'Keller','5': 'Lantern', '6': 'Olson', '7': 'Collins', 			'8': 'Weinstein', '9': 'Negron'}

while True:
	randomNum = random.randint(0,9)
	print('Type in the number above and press ENTER')
	numNum = input()
	if numNum == '':
		break
	
	
	if numNum in firstName:
		print('Your random name is: ', firstName[numNum], lastName[numNum])
		break
	else: 
		print('I am a turkey')

		

		
