#Find the occurences of a character in a list

names=["Alice","Bob","Charlie","David","Eva","Frank","Grace"]

count_a=0
for name in names:
	count_a+=name.lower().count('a')

print"The letter 'a' occurs {0} times in the list of names".format(count_a)
