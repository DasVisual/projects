#! python3

import pandas as pd
import matplotlib.pyplot as plt
import csv

user_ids = []
while True:
	# Allows user to input values and appends list and breaks
	user_input = str(input('Type number for user id (Enter nothing to stop)'))
	if user_input:
		user_ids.append(user_input)
		print(user_ids)
	if user_input == '':
		break	
#excuse_full = 'A randomly generated excuse: ' + random.choice(user_ids)

with open('user_id.csv', 'wb') as f:
	for line in user_ids:
		f.write(line)
	
	
	
	
	
	# for line in user_ids:
		# file.write(line)
		# file.write('\n')
