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

