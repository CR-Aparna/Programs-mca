#word count
line=raw_input("Enter a line of text:")
words=line.lower().split() 
word_count={} #create a dictionary to count occurences
for word in words:
	if word in word_count:
		word_count[word]+=1
	else:
		word_count[word]=1
#display
print("Word occurences:")
for word,count in word_count.items():
	print (word),":",(count)
