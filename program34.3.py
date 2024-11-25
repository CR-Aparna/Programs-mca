from graphics.rectangle import *
from graphics.circle import *
from graphics.ThreeD_graphics.cuboid import *
from graphics.ThreeD_graphics.sphere import *

length=5
breadth=3
print"Rectangle Area:",r_area(length,breadth)
print"Rectangle Perimeter:",r_perimeter(length,breadth)

radius=7
print"Circle Area:",c_area(radius)
print"Circle Perimter:",c_perimeter(radius)

height=4
print"Cuboid Area:",cu_area(length,breadth,height)
print"Cuboid Perimeter:",cu_perimeter(length,breadth,height)

print"Sphere Area:",s_area(radius)
print"Sphere perimter:",s_perimeter(radius)

