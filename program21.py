# Check if integer list contains values greater than 100

input_values =raw_input("Enter a list of integers separated by spaces")

int_list = [int(num) for num in input_values.split()]
modified_list = ['over' if num>100 else num for num in int_list]

print"Modified list:",modified_list
