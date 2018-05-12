#! python 3



# strip song names of ending

import os, re


# splits the lines into parts
songs = set()

with open('C:/Users/Mohammed/Downloads/python/projects/aToBeCompleted/audioAbdul/songs2.txt', encoding='utf-8') as file:
	for line in file:
		values = line.split()
		print(values[0:9])		
		

# Finds the pattern of .mp3 in file		
pattern = re.compile('.mp3')
for i, line in enumerate(open('C:/Users/Mohammed/Downloads/python/projects/aToBeCompleted/audioAbdul/songs2.txt')):
	for match in re.finditer(pattern, line):
		print('Found on line %s: %s' % (i+1, match.groups()))

	
		
# generate bpm randomly



# generate graphs bpm/tempo, keys