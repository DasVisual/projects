#! python 3

# another version of temperature checker, hopefully no none result

print('What is the current temperature of the chicken?')

def checkTemp(Temp):
    if Temp > 260:
        return 'It is probably cooked'
    elif Temp < 260:
        return 'More heat more time'


Temp = int(input())
Result = checkTemp(Temp)
print(Result)

