#selective imports

from graphics.rectangle import r_area as rect_area,r_perimeter as rect_perimeter
from graphics.circle import c_area as circ_area,c_perimeter as circ_perimeter
from graphics.ThreeD_graphics.cuboid import cu_area as cuboid_area,cu_perimeter as cuboid_perimeter
from graphics.ThreeD_graphics.sphere import s_area as sphere_area,s_perimeter as sphere_perimeter

length=5
breadth=3
print"Rectangle area:",rect_area(length,breadth)
print"Rectangle perimeter:",rect_perimeter(length,breadth)

radius=7
print"Circle area:",circ_area(radius)
print"Circle perimeter:",circ_perimeter(radius)

height=4
print"Cuboid area:",cuboid_area(length,breadth,height)
print"Cuboid perimeter:",cuboid_perimeter(length,breadth,height)

print"Sphere area:",sphere_area(radius)
print"Sphere perimeter:",sphere_perimeter(radius)
