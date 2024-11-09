#Accept a list of words and return the longest word

input_string=raw_input("Enter a list of words separated by spaces:")
words=input_string.split()
longest_word= " "
longest_length=0
for word in words:
	if len(word)>longest_length:
		longest_length=len(word)
		longest_word=word
print "Length of the longest word is:",longest_length
print "Longest word is:",longest_word

