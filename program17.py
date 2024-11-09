#GCD Calculation

def find_gcd(num1,num2):
	while num2:
		num1 , num2= num2 , num1 % num2
	return num1
number1 = 56
number2 = 98

gcd = find_gcd(number1,number2)
print("The GCD of {} and {} is :{}".format(number1,number2,gcd))
