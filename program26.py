#Generate a list of four digit numbers in a given range with all their digits even and the number is a perfect square

def is_all_even_digits(n):
	return all(int(digit) % 2 == 0 for digit in str(n))
def generate_even_digit_squares(start,end):
	even_digit_squares =[]
	start_sqrt = int(start**0.5)
	end_sqrt = int(end**0.5)+1
	for i in range (start_sqrt,end_sqrt):
		square = i*i
		if square>=start and square<=end and is_all_even_digits(square):
			even_digit_squares.append(square)
	return even_digit_squares
start_range = 1000
end_range = 9999

result = generate_even_digit_squares(start_range,end_range)
print "The four-digit numbers that are perfect squares with all even digits are:",result

