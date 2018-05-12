#! python 3


# Ask what the temperature is
print('What is the current temperature (fahrenheit) of the chicken?')

# TODO: Define temperature and variables


def checktemp(Temp):
    if Temp >= 260:
        return('''That's the right temp. Turn off the oven''')
    elif Temp < 260:
        return('Cook the chicken some more :)')

Temp = int(input())
Result = checktemp(Temp)
print(Result)

# TODO: Compare input with standards

# TODO: print whether temp needs to be higher or lower
