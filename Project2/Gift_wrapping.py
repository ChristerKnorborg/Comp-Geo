from Orientation import orientation
from Shared import Point, print_points, sort_by_x_coordinate


def gift_wrapping(points):

    n = len(points)
    if n <= 2:
        return

    #Find lowest index by first finding the lowest value.
    #This takes O(n) + O(n) and thus better than sorting.
    lowest_val = min(p.x for p in points)
    lowest_x = next((i for i, p in enumerate(points) if p.x == lowest_val), -1)

    # find highest x val for stop critiria. We only compute upper hall
    highest_val = max(p.x for p in points)
    highest_x = next((i for i, p in enumerate(points) if p.x == highest_val), -1)

    hull = []

    # start index s, current i and next j
    i = lowest_x
    j = 0
    
    while(True):
        
        hull.append(points[i])

        j = (i + 1) % n

        for k in range(n):  
            # if left turn, then update next point to be wrapped (j) to new smallest angle
            if orientation(points[i], points[k], points[j]) == 2:
                j = k

        # at the end of the loop, the current is set to the next index
        i = j

        
        if i == lowest_x:
            break
                
    return hull



# Test gift_wrapping
p1 = Point(6, 4)
p2 = Point(2, 1)
p3 = Point(2, 3)
p4 = Point(4, 3)
p5 = Point(4, 4)
p6 = Point(6, 2)
p7 = Point(1, 1)
p8 = Point(7, 3)
p9 = Point(8, 2)

test_list = [p1,p2,p3,p4,p5,p6,p7,p8,p9]

upper_hull = gift_wrapping(test_list)
print_points(upper_hull)



            