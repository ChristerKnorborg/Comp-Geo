class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        

    
# inbuilt python method for sorting, which runs in n log n time complexity
def sort_by_x_coordinate(points):
    points.sort(key=lambda p: (p.x, p.y))

def get_leftmost_point_idx(points):
    min_idx = 0
    for idx, _ in enumerate(points):
        if points[idx].x < points[min_idx].x:
            min_idx = idx
        elif points[idx].x == points[min_idx].x:
            if points[idx].y < points[min_idx].y:
                min_idx = idx 
    return min_idx

def get_rightmost_point_idx(points):
    max_idx = 0
    for idx, _ in enumerate(points):
        if points[idx].x > points[max_idx].x:
            max_idx = idx
        elif points[idx].x == points[max_idx].x:
            if points[idx].y > points[max_idx].y:
                max_idx = idx 

    return max_idx



# This method decides if a straight turn (from the anchor_point
# through the best_point to the new_point) result in the new_point
# being better suited. If that is the case the method returns true.
def straight_update_check(anchor_point, best_point, new_point):
    

    # if line from bottom left to top right check
    # anchor_point(x,y) < best_point(x,y) < new_point(x,y)
    if anchor_point.x < best_point.x and anchor_point.y < best_point.y:
        if best_point.x < new_point.x and best_point.y < new_point.y:
            return True

    # if line from top left to bottom right check
    # anchor_point(x) < best_point(x) < new_point(x)
    # new_point(y) < best_point(y) < anchor_point(y)
    elif anchor_point.x < best_point.x and anchor_point.y > best_point.y:
        if best_point.x < new_point.x and best_point.y > new_point.y:
            return True

    # if line from left to right check
    # anchor_point(x) < best_point(x) < new_point(x)
    # new_point(y) = best_point(y) = anchor_point(y)
    elif anchor_point.x < best_point.x and anchor_point.y == best_point.y: 
        if best_point.x < new_point.x and best_point.y == new_point.y:
            return True

    # if line from bottom to top check (opposite check is not needed as upper hulls stop in top left corner)
    # anchor_point(y) < best_point(y) < new_point(y)
    # new_point(x) = best_point(x) = anchor_point(x)
    elif anchor_point.y < best_point.y and anchor_point.x == best_point.x:  
        if best_point.y < new_point.y and best_point.x == new_point.x:
            return True


    else:
         return False


def print_points(points):
    for p in points:
        print(p.x, p.y)


