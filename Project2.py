from cgi import test
from cmath import inf
from typing import List


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
 


def orientation(p1, p2, p3):
     
    # to find the orientation of
    # an ordered triplet (p1,p2,p3)
    # function returns the following values:
    # 0 : Collinear points
    # 1 : Clockwise points
    # 2 : Counterclockwise
    val = (float(p2.y - p1.y) * (p3.x - p2.x)) - \
           (float(p2.x - p1.x) * (p3.y - p2.y))
    if (val > 0):
         
        # Clockwise orientation
        print("Right Turn")
    elif (val < 0):
         
        # Counterclockwise orientation
        print("Left Turn")
    else:
         
        # Collinear orientation
        print("No Turn")


def orientation_test(p1, p2, p3):
     
    val = (float(p1.x * (p2.y - p3.y)) + float(p2.x * (p3.y-p1.y)) + float(p3.x * (p1.y-p2.y)))

    if (val < 0):
        # Right
        print("Right Turn")
        return 1
    elif (val > 0):
        # Left
        print("Left Turn")
        return 2
    else:
        # Straight
        print("No Turn")
        return 0
 



# Test
p1 = Point(0, 0)
p2 = Point(1, 2)
p3 = Point(4, 4)
 
orientation_test(p1, p2, p3)
orientation(p1, p2, p3)
print("should turn right")


# Test
p1 = Point(1, 1)
p2 = Point(2, 1)
p3 = Point(2, 3)
print("LEFT TURN")
orientation_test(p1, p2, p3) 
orientation(p1, p2, p3)


# Test
p1 = Point(8, 1)
p2 = Point(9, 2)
p3 = Point(11, 3)
 
orientation_test(p1, p2, p3) 
orientation(p1, p2, p3)
print("should turn right")

# Test
p1 = Point(0, 0)
p2 = Point(2, 4)
p3 = Point(3, 9)
 
orientation_test(p1, p2, p3) 
orientation(p1, p2, p3)
print("should turn left")

 



def grahams_scan(points):
    upper_hull = []

    #sort by x-coordinate and append 2 lowest points to upper hall
    sort_by_x_coordinate(points)
    upper_hull.append(points[0])
    upper_hull.append(points[1])



    for i in range (2, len(points)):
        while len(upper_hull) >= 2 and orientation_test(upper_hull[len(upper_hull)-2], upper_hull[len(upper_hull)-1], points[i]) == 2:
            del upper_hull[len(upper_hull)-1]
        upper_hull.append(points[i])

    return upper_hull


    
def gift_wrapping(points):
    print("gift wrap")
    # append leftmost x-coordinate to upper hull
    upper_hull = []
    start_index = 0
    current_point_index = 0
    

    
    while(True):
        
        upper_hull.append(points[current_point_index])

        next_point_index = current_point_index + 1 % len(points)

        for i in range(len(points)-1):
            # if left turn, then update next_point_index to new smallest angle
            if orientation_test(points[current_point_index], points[i], points[next_point_index]) == 2:
                next_point_index = i

        # at the end of the loop, the current is set to the next index
        current_point_index = next_point_index

        if current_point_index == start_index:
            break
                
    return upper_hull
            
        

    

    


    

def sort_by_x_coordinate(points):
    points.sort(key=lambda p: p.x)



def print_points(points):
    for p in points:
        print(p.x, p.y)




tester =[p3, p1, p2]
print("Før:")
print_points(tester)
sort_by_x_coordinate(tester)
print("Efter:")
print_points(tester)



# Test grahams_scan
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

upper_hull = grahams_scan(test_list)
print_points(upper_hull)




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















