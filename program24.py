#Generate fibonacci series of n terms

def fibonacci_iterative(n):
	fib_series=[]
	a,b =0,1
	for i in range(n):
		fib_series.append(a)
		a,b = b,a+b
	return fib_series
num_terms = int(input("Enter the number of terms for the fibonacci series:"))
result = fibonacci_iterative(num_terms)
print"The fibonacci series for {} terms is {} ".format(num_terms,result)
