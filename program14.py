#Print colors in one list which is not in another list

color_list1 =["red","green","blue","yellow","purple"]
color_list2 =["blue","yellow","orange"]

unique_colors =[color for color in color_list1 if color not in color_list2]

print"Colors in color_list1 not in color_list2:",unique_colors
