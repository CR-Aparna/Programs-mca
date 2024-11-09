#list comprehensions
 
N=int(input("Enter the value of N:"))

#List comprehension to generate squares of numbers from 0 to N-1
 
Squares=[x**2 for x in range(N)]
print"Squares of first", N ,"numbers:",Squares
