import numpy as np
import matplotlib.pyplot as plt

from Orientation import orientation
from Shared import Point, sort_by_x_coordinate
from Generate_data import gen_circle_data, gen_square_data, gen_curve_data, make_points_from_numpy


def grahams_scan(points) -> list:
    
    # more than 2 points required for upper hull
    n = len(points)
    if n <= 2:
        return []

    upper_hull = []


    #sort by x-coordinate and append 2 lowest points to upper hall
    sort_by_x_coordinate(points)


    upper_hull.append(points[0])
    upper_hull.append(points[1])


    for i in range (2, n):

        # loop through the sorted points and add them to upper hull,
        # if orientation through last 2 points and current point doesn't make a right turn
        while len(upper_hull) >= 2 and orientation(upper_hull[len(upper_hull)-2], 
                                                   upper_hull[len(upper_hull)-1],
                                                   points[i]) != 1:
            del upper_hull[len(upper_hull)-1]
        upper_hull.append(points[i])

    return upper_hull
