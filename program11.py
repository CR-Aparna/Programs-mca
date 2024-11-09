#Replace teh character in a string
input_string=raw_input("Enter a string:")
input_string=input_string.lower()
if input_string:
	first_char=input_string[0]
        modified_string=first_char + input_string[1:].replace(first_char,'$')
        print"Modified string:",modified_string
else:
	print"Empty string provided"
