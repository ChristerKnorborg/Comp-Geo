from cgi import test
from cmath import inf
from typing import List


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    

def sort_by_x_coordinate(points):
    points.sort(key=lambda p: p.x)



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




















