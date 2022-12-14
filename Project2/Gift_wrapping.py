from Orientation import orientation
from Shared import get_leftmost_point_idx, get_rightmost_point_idx, straight_update_check


def gift_wrapping(points):

    # more than 2 points required for upper hull
    n = len(points)
    if n <= 2:
        return

    # find start point and end point
    min_idx = get_leftmost_point_idx(points)
    max_idx = get_rightmost_point_idx(points)

    hull = []

    max_x = points[max_idx].x
    max_y = points[max_idx].y

    i = min_idx
    j = 0
    
    while(True):


        hull.append(points[i])

        # mod to prevent out of bounds issues for j 
        j = (i + 1) % n

        # update next point j to to lowest angle by checking all points for left turn
        for k in range(n):  
            turn = orientation(points[i], points[j], points[k])
            if turn == 2:
                j = k
            elif turn == 0:
                if straight_update_check(points[i], points[j], points[k]):
                    j = k 
                    

        # at the end of the loop, the current (i) is set to the next index (j)
        i = j
        
        # Breaks the algorithm after upper hull by using max_idx. 
        # Using the values in case of points with same max val. 
        if points[i].x == max_x and points[i].y == max_y:
            hull.append(points[i])
            break
                
    return hull





            