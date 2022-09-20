from Shared import Point

def orientation(p1, p2, p3):
     
    val = (float(p1.x * (p2.y - p3.y)) + float(p2.x * (p3.y-p1.y)) + float(p3.x * (p1.y-p2.y)))

    if (val < 0):
        # Right
        return 1
    elif (val > 0):
        # Left
        return 2
    else:
        # Straight
        return 0
 


# Test
p1 = Point(0, 0)
p2 = Point(1, 2)
p3 = Point(4, 4)
 
orientation(p1, p2, p3)
print("should turn right")


# Test
p1 = Point(1, 1)
p2 = Point(2, 1)
p3 = Point(2, 3)
print("LEFT TURN")
orientation(p1, p2, p3)


# Test
p1 = Point(8, 1)
p2 = Point(9, 2)
p3 = Point(11, 3)
 
orientation(p1, p2, p3) 
print("should turn right")

# Test
p1 = Point(0, 0)
p2 = Point(2, 4)
p3 = Point(3, 9)
 
orientation(p1, p2, p3) 
print("should turn left")