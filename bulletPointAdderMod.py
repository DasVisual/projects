#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

import random

# Separate lines and add stars.
lines = text.split('\n') 
for i in range(len(lines)):     # loop through all indexes in the 'lines' list
    lines[i] = str(random.randint(0, 10)) + ' ' + lines[i]  # add star to each string in 'lines' list
text = '\n'.join(lines)
pyperclip.copy(text)
print('''Hellooo, what you have copied will have $$ before every line, as a bullet point; 
jk now it generates random integers before the line''')
