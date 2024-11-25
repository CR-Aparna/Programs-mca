#regular import

import graphics.rectangle
import graphics.circle
import graphics.ThreeD_graphics.cuboid
import graphics.ThreeD_graphics.sphere

length=5
breadth=3
print"Rectangle Area:",graphics.rectangle.r_area(length,breadth)

print"Rectangle Perimeter:",graphics.rectangle.r_perimeter(length,breadth)

radius=7
print"Circle Area:",graphics.circle.c_area(radius)
print"Circle Perimeter:",graphics.circle.c_perimeter(radius)

height=4
print"Cuboid Area:",graphics.ThreeD_graphics.cuboid.cu_area(length,breadth,height)
print"Cuboid Perimeter:",graphics.ThreeD_graphics.cuboid.cu_perimeter(length,breadth,height)

print"Sphere Area:",graphics.ThreeD_graphics.sphere.s_area(radius)
print"Sphere perimeter:",graphics.ThreeD_graphics.sphere.s_perimeter(radius)

