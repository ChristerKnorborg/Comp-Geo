from Orientation import orientation
from Shared import Point, print_points, sort_by_x_coordinate, get_leftmost_point_idx, get_rightmost_point_idx


def gift_wrapping(points):

    # need more than 2 points for hull
    n = len(points)
    if n <= 2:
        return

    # find start point
    min_idx = get_leftmost_point_idx(points)

    # find highest x val for stop critiria. We only compute upper hall
    max_idx = get_rightmost_point_idx(points)


    hull = []

    # start index s, current i and next j
    i = min_idx
    j = 0
    
    while(True):
        print(points[i].x)
        hull.append(points[i])

        j = (i + 1) % n

        for k in range(n):  
            # if left turn, then update next point to be wrapped (j) to new smallest angle
            if orientation(points[i], points[j], points[k]) == 2:
                j = k

        # at the end of the loop, the current (i) is set to the next index (j)
        i = j
        
        # breaks the algorithm after upper hull. 
        # If changed to min_idx and append removed the whole hull is computed.
        if i == max_idx:
            hull.append(points[i])
            break
                
    return hull



# Test gift_wrapping
#p1 = Point(6, 4)
#p2 = Point(1, 2)
#p3 = Point(2, 3)
#p4 = Point(4, 3)
#p5 = Point(4, 4)
#p6 = Point(6, 2)
#p7 = Point(1, 1)
#p8 = Point(7, 3)
#p9 = Point(8, 2)

#test_list = [p1,p2,p3,p4,p5,p6,p7,p8,p9]

#upper_hull = gift_wrapping(test_list)
#print_points(upper_hull)



            