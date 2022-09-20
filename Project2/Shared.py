from cgi import test
from cmath import inf
import operator
from typing import List


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    

def sort_by_x_coordinate(points):
    points.sort(key=lambda p: (p.x, p.y))


def get_leftmost_point_idx(points):
    min_idx = 0
    for idx, p in enumerate(points):
        if points[idx].x < points[min_idx].x:
            min_idx = idx
        elif points[idx].x == points[min_idx].x:
            if points[idx].y < points[min_idx].y:
                min_idx = idx 

    return min_idx

def get_rightmost_point_idx(points):
    max_idx = 0
    for idx, p in enumerate(points):
        if points[idx].x > points[max_idx].x:
            max_idx = idx
        elif points[idx].x == points[max_idx].x:
            if points[idx].y > points[max_idx].y:
                max_idx = idx 

    return max_idx


def print_points(points):
    for p in points:
        print(p.x, p.y)




##tester =[p3, p1, p2]
#print("Før:")
#print_points(tester)
#sort_by_x_coordinate(tester)
#print("Efter:")
##print_points(tester)
##




















