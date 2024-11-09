#Display the given pyramid with step number accepted from user
try:
	n= int(raw_input("Enter the number of steps(N):"))
	for i in range(1,n+1):
		row=[]
		for j in range(1,i+1):
			row.append(i*j)
		print " ".join(map(str,row))
except ValueError:
	print "Please enter a valid integer."


