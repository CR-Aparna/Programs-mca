#CREATE A STRING WITH CHARACTERS EXCHANGED

input_string = raw_input("Enter a string:")

if len(input_string)>1:
	modified_string = input_string[-1]+input_string[1:-1]+input_string[-0]
else:
	modified_string = input_string
print"Modified string :",modified_string
