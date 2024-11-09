#find factorial of a number

def factorial_recursive(n):
	if n==0 or n==1:
		return 1
	else:
		return n*factorial_recursive(n-1)
num = int(input("Enter a number:"))
result = factorial_recursive(num)
print"The factorial of {} is {}".format(num,result) 
