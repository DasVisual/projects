#! python3

'''Generates random responses'''

import random
from time import strftime


# prints a random choice
times = ['5', '10', '25', '45']
options = ['Call back in ' + random.choice(times) + 'min','Text me','Leave a voicemail']
time = '''\n"This was sent at: ''' + strftime('''%a, %d %b %Y %H:%M:%S"''')
print(random.choice(options), time)

