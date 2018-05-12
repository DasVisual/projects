#! python3

def calculate_kg_to_lbs(kg):
	answer = (kg) * (2.2)
	print(answer)

print('Enter your weight in kilograms')	
kg = int(input())
print('Your weight in pounds is: ')
calculate_kg_to_lbs(kg)
