from Orientation import orientation
from Shared import Point, print_points, sort_by_x_coordinate


def gift_wrapping(points):

    upper_hull = []
    start_index = 0
    current_point_index = 0
    
    while(True):
        
        upper_hull.append(points[current_point_index])

        next_point_index = current_point_index + 1 % len(points)

        for i in range(len(points)-1):
            # if left turn, then update next_point_index to new smallest angle
            if orientation(points[current_point_index], points[i], points[next_point_index]) == 2:
                next_point_index = i

        # at the end of the loop, the current is set to the next index
        current_point_index = next_point_index

        if current_point_index == start_index:
            break
                
    return upper_hull



# Test gift_wrapping
p1 = Point(1, 1)
p2 = Point(2, 1)
p3 = Point(2, 3)
p4 = Point(4, 3)
p5 = Point(4, 4)
p6 = Point(6, 2)
p7 = Point(6, 4)
p8 = Point(7, 3)
p9 = Point(8, 2)

test_list = [p1,p2,p3,p4,p5,p6,p7,p8,p9]

upper_hull = gift_wrapping(test_list)
print_points(upper_hull)



            