from Shared import Point

def orientation(p1, p2, p3):
    #Calculate determinant from 3 points
    val = (float(p1.x * (p2.y - p3.y)) + float(p2.x * (p3.y-p1.y)) + float(p3.x * (p1.y-p2.y)))

    if (val < 0):
        # Right turn
        return 1
    elif (val > 0):
        # Left turn
        return 2
    else:
        # Straight (no turn)
        return 0
