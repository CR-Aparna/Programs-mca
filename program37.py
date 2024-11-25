#Rectangle with private attributes length and width

class Rectangle:
	def __init__(self,length,width):
		self._length = length
		self._width = width
	def area(self):
		return self._length*self._width
	def __lt__(self,other):
		if isinstance(other,Rectangle):
			return self.area()<other.area()
		return NotImplemented
	def get_details(self):
		return "Length : {0} , Width : {1} , Area : {2}".format(self._length,self._width,self.area())

rect1 = Rectangle(4,5)
rect2 = Rectangle(6,3)

print "Rectangle 1 :",rect1.get_details()
print "Rectangle 2 :",rect2.get_details()

if rect1 < rect2:
	print "Rectangle 1 has a smaller area than rectangle 2."
else:
	print "Rectangle 1 has a larger area than Rectangle 2."

