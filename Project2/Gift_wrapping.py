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

    max_x = points[max_idx].x
    max_y = points[max_idx].y

    i = min_idx
    j = 0
    
    while(True):


        hull.append(points[i])

        # mod to prevent out of bounds issues for j

        j = (i + 1)

        # update next point j to to lowest angle by checking all points for left turn
        for k in range(n):  
            turn = orientation(points[i], points[j], points[k])
            if turn == 2:
                j = k
            elif turn == 0:

                if points[i].x < points[j].x and points[i].y < points[j].y:
                    if points[j].x < points[k].x and points[j].y < points[k].y:
                        j = k

                elif points[i].x < points[j].x and points[i].y > points[j].y:
                    if points[j].x < points[k].x and points[j].y > points[k].y:
                        j = k

                elif points[i].x < points[j].x:  
                    if points[j].x < points[k].x:
                        j = k

                elif points[i].y < points[j].y:  
                    if points[j].y < points[k].y:
                        j = k 
                    

        # at the end of the loop, the current (i) is set to the next index (j)
        i = j
        
        # breaks the algorithm after upper hull by using max_idx. 
        if points[i].x == max_x and points[i].y == max_y:
            hull.append(points[i])
            break
                
    return hull





            