#list comprehensions
word= raw_input("Enter a word:")
#Extract vowels from the word
vowels=[letter for letter in word if letter.lower() in 'aeiou']
#display
print"Vowels in the word are",vowels
