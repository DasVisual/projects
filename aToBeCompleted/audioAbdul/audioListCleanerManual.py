#! python 3



# strip song names of ending
# ^^Did this manually using replace--non python 
import os, re, random





# bpm??


	
		
# generate keys randomly
randomNum = random.randint(1,7)
keys =  ['A', 'B', 'C', 'D',
		'E', 'F', 'G']

def printRandNum(randomNum):
	if randomNum in keys:
		print(keys[randomNum])
	else:
		return('The number is not in the list or does not work')

print(keys[randomNum])



# add letters to beginning of lines
output = ""
file_name = 'C:/Users/Mohammed/Downloads/python/projects/aToBeCompleted/audioAbdul/songs3.txt'
string_to_add = keys[randomNum]

with open(file_name, 'r') as file:
    file_lines = [''.join([x.strip(), '\n', string_to_add]) for x in file.readlines()]

with open(file_name, 'w') as file:
    file.writelines(file_lines) 


# generate graphs bpm/tempo, keys

