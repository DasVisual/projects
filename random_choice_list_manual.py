#! python3

import random
from time import strftime

'''Re-writing randomchoicelist to make it suitable for user input all variables'''

print('This program helps you setup your automated voicemail')

'''# Ask for random choices

print('What random times would you like for callback?')
input_times = input()

times = [input_times]'''

# times = {}
# counter = 1
# while True:
	# input_times = input('''What random times do you want? (Type 'done' to quit)''')
	# if input_times == 'done':
		# break
	# times[counter] = input_times
	# counter += 1
	
# print(times.items())
# print(random.choice(times))

times = []
counter = 1
while True:
	# Allows user to input values and appends list and breaks
	user_input = input('Type random TIME (4 entries-digit only)')
	if user_input:
		times.append(user_input)
		print(times)
	counter += 1
	if counter == 5:
		break
#time_full = 'A randomly generated time: ' + random.choice(times)
time_full = random.choice(times)

excuses = []
while True:
	# Allows user to input values and appends list and breaks
	user_input = str(input('Type random EXCUSE (Enter nothing to stop)'))
	if user_input:
		excuses.append(user_input)
		print(excuses)
	if user_input == '':
		break	
#excuse_full = 'A randomly generated excuse: ' + random.choice(excuses)
excuse_full = random.choice(excuses)

print('Your randomly generated excuse is: ', excuse_full, 'in', time_full, 'min')
 
# # prints a random choice
# '''times = ['5', '10', '25', '45']
# options = ['Call back in ' + random.choice(times) + 'min','Text me','Leave a voicemail']
# time = '''\n"This was sent at: ''' + strftime('''%a, %d %b %Y %H:%M:%S"''')
# print(random.choice(options), time)'''