
from cmath import log

from Graham_scan import grahams_scan
from Shared import get_leftmost_point_idx, get_rightmost_point_idx


def chan_algorithm(points):


    n = len(points)
    for i in range(log(log(n))):
        if (upper_hall_with_size(points,2**(2**i))):
            break




    def upper_hall_with_size(points,h):

        for i in range(len(0, n, h)):
            partitions = points[i:i+h]
        

        partition_hulls = []

        m = n/h

        for i in range(m):
            partition_hulls + grahams_scan(partitions[i])

        upper_hull = []

        p = get_leftmost_point_idx(partition_hulls)
        max_coordinate = get_rightmost_point_idx(partition_hulls)

        for i in range(h):
            upper_hull.append(p)

            if p == max_coordinate:
                break

            tangents = []    
            for i in range(m):
                tangents.append(compute_tanget(p,partition_hulls[i]))

            


            
def compute_tanget(point,points):

    tangent = "dummy"
    return tangent
        


    
