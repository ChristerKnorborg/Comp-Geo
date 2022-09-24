from math import floor
from turtle import left
from Gift_wrapping import gift_wrapping
from Shared import Point

p1 = Point(1, 1)
p2 = Point(1, 2)
p3 = Point(2, 3)
p4 = Point(4, 3)
p5 = Point(4, 4)
p6 = Point(6, 2)
p7 = Point(6, 4)
p8 = Point(7, 3)
p9 = Point(8, 2)
p10 = Point(8, 3)

inner_list1 = [p1,p2,p3,p4,p5]
inner_list2 = [p6,p7,p8,p9,p10]
partition_upper_hulls = []
partition_upper_hulls.append(inner_list1)
partition_upper_hulls.append(inner_list2)

best = p6


print(partition_upper_hulls)
partition_upper_hulls = [[point for point in outer if point.x >= best.x] for outer in partition_upper_hulls]
print(partition_upper_hulls)
