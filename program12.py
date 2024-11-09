#COMPARE TWO LISTS

list1=list(map(int,raw_input("Enter the first list of integers (space-separated):").split()))
list2=list(map(int,raw_input("Enter the second list of integers (space-separated):").split()))

same_length = len(list1)==len(list2)
same_sum = sum(list1)==sum(list2)
common_values=set(list1) & set(list2)

print"a)Are the lists of the same length?",same_length
print"b)Do the lists sum to the same value?",same_sum
print"c)Do any values occur in both lists?",bool(common_values)
 
if common_values:
	print"Common values:",common_values 
