from Orientation import orientation
from Shared import get_leftmost_point_idx, get_rightmost_point_idx


def gift_wrapping(points):

    # more than 2 points required for upper hull
    n = len(points)
    if n <= 2:
        return

    # find start point and end point
    min_idx = get_leftmost_point_idx(points)
    max_idx = get_rightmost_point_idx(points)

    hull = []


    i = min_idx
    j = 0
    
    while(True):
        hull.append(points[i])

        j = i + 1

        # update next point j to to lowest angle by checking all points for left turn
        for k in range(n):  
            if orientation(points[i], points[j], points[k]) == 2:
                j = k

        # at the end of the loop, the current (i) is set to the next index (j)
        i = j
        
        # breaks the algorithm after upper hull by using max_idx. 
        if i == max_idx:
            hull.append(points[i])
            break
                
    return hull





            