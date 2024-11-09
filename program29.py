#Add "ing" at the end of a given string if it already ends with 'ing' then 'ly'

input_string = raw_input("Enter a string:")
if input_string .endswith("ing"):
	result_string=input_string+"ly"
else:
	result_string=input_string+"ing"
print"Resulting string:",result_string

