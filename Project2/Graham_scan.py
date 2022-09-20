from Orientation import orientation
from Shared import Point, print_points, sort_by_x_coordinate


def grahams_scan(points):
    n = len(points)
    if n <= 2:
        return

    upper_hull = []

    #sort by x-coordinate and append 2 lowest points to upper hall
    sort_by_x_coordinate(points)
    upper_hull.append(points[0])
    upper_hull.append(points[1])


    for i in range (2, n):
        while len(upper_hull) >= 2 and orientation(upper_hull[len(upper_hull)-2], 
                                                   upper_hull[len(upper_hull)-1],
                                                   points[i]) != 1:
            del upper_hull[len(upper_hull)-1]
        upper_hull.append(points[i])

    return upper_hull





# Test grahams_scan
p1 = Point(1, 1)
p2 = Point(1, 2)
p3 = Point(2, 3)
p4 = Point(4, 3)
p5 = Point(4, 4)
p6 = Point(6, 2)
p7 = Point(6, 4)
p8 = Point(7, 3)
p9 = Point(8, 2)

test_list = [p1,p2,p3,p4,p5,p6,p7,p8,p9]

upper_hull = grahams_scan(test_list)
print_points(upper_hull)