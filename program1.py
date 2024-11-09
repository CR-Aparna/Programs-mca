current_year=int(input("Enter the current year:"))
final_year=int(input("Enter the final year"))
#initialize an empty list to store leap years
 
leap_years=[]
for year in range(current_year,final_year+1):
	#checking
	if(year%4==0 and year%100!=0) or (year%400==0):
		leap_years.append(year)
print "Leap years are:",leap_years
