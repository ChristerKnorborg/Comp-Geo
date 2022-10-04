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





            