#Print the Extension of a file

filename=raw_input("Enter the filename")

if '.' in filename:
	extension=filename.split('.')[-1]
	print"The extension of the file is:",extension
else:
	print"The file has no extension."
