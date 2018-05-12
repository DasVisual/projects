#! python 3

# Graphic show stats about how many songs at each bpm/key
# bubble size shows how many songs there are, color shows key
###########

# +songs = set()
# +
# +with open("songs.txt", encoding='utf-8') as file:
# +    for line in file:
# +        # remove crap
# +        clean = line.strip(' ')
# +        clean = clean.strip('\r')
# +        clean = clean.strip('\n')
# +        clean = clean.strip('\"')
# +
# +        # get filename only
# +        last_dot = clean.rfind('.')
# +        length = last_dot if last_dot >= 0 else len(clean)
# +        name = clean[:length]
# +
# +        # store
# +        songs.add(name)
# +
# +sorted_set = sorted(songs, key=str.lower)


import random

f = open('testyfile.txt', 'w+')

for i in range(10):
	f.write('This is line %d\r\n' % (i+1))
	
	

songs = set()

# Get file name of songs from text file, no duplicates



# random number generator w seed--later integrate into a prefix
# https://www.bing.com/search?q=repeating+function+python&src=IE-SearchBox&FORM=IESR4A&pc=UE00
#
while True:
	print(random.randrange(100, 1000, 2))
	if x = 100:
		break
		
# Generate bpm/key



# Generate graph, 1 per key CDEFGAB



# extra: fetch list from url


