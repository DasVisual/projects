#! Python 3
#job_titles = {'0': 'the Manicurist', '1': 'the Sorcerer', '2': 'the Witness', '3': 'the Accountant', '4': 'the Clown'}

job_titles = {'0': 'the Tryhard', '1': 'the Sprinter', '2': 'the Shard', '3': 'the Raptor', 
			'4': 'the Sorcerer'}

print('What is your first name?')

firstname = str(input())

print('What is your last name?')

lastname = str(input())

while True:
    print('Enter a number: (blank to quit)')
    number = input()
    if number == '':
        break

    if number in job_titles:
        print('Your name is: ', firstname, lastname, job_titles[number])
        break
    else:
        print('Enter a number from 0 to 4 ' + firstname)
