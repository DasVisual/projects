#! python 3 

# ask for the first name
print('What is your first name strangerrr?')
firstname = str(input())


# ask for the last name
print('What is your last name?')

lastname = str(input())

# list of random funny names/job titles

print('Type a number from 0 to 6 and press ENTER')


def funnyjobs(number):
    if number == 0:
        return 'the Cowboy'
    elif number == 1:
        return 'the Stripper'
    elif number == 2:
        return 'the Magician'
    elif number == 3:
        return 'the Belly Dancer'
    elif number == 4:
        return 'the Farming Disco'
    elif number == 5:
        return 'the Astronaut/Pilot'
    elif number == 6:
        return 'the Panda 🐼 <--(that is you)'


number = int(input())


# print the first and last name

print('You are: ', firstname, lastname, funnyjobs(number))