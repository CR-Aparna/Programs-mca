#Biggest of 3 numbers entered
 
num1=float(input("Enter the first number"))
num2=float(input("Enter the second number"))
num3=float(input("Enter the third number"))

largest_number=num1

if num2>largest_number:
	largest_number=num2
if num3>largest_number:
	largest_number=num3

print"The largest number is :",largest_number

	

