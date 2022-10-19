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



# This method decides if a straight turn should result
# in an update for 
def calc_straight_turn_behavior(p1,p2,p3):
    
    if p1.x < p2.x and p1.y < p2.y:
        if p2.x < p3.x and p2.y < p3.y:
            return True

    elif p1.x < p2.x and p1.y > p2.y:
        if p2.x < p3.x and p2.y > p3.y:
            return True

    elif p1.x < p2.x:  
        if p2.x < p3.x:
            return True

    elif p1.y < p2.y:  
        if p2.y < p3.y:
            return True


    else:
         return False


def print_points(points):
    for p in points:
        print(p.x, p.y)


