
from cmath import log

from Graham_scan import grahams_scan
from Shared import get_leftmost_point_idx, get_rightmost_point_idx, divide_list_into_chunks


def chan_algorithm(points):

    def upper_hall_with_size(points,h):

        n = len(points)
        m = n/h


        partition = list(divide_list_into_chunks(points, m))
        
        # find upper hull for all m partitions
        partition_upper_hulls = []
        for i in range(m):
            partition_upper_hulls.append(grahams_scan(partition[i]))


        upper_hull = []

        p = get_leftmost_point_idx(points)
        max_coordinate = get_rightmost_point_idx(points)

        l = ray(p)

        for i in range(h):

            upper_hull.append(p)

            if p == max_coordinate:
                break

            tangents = []    
            for i in range(m):
                tangents.append(compute_tanget(p, partition_upper_hulls[i]))

            t = min(tangents)

            p = tangent.other_point
            l = t

            for i in range(len(partition_upper_hulls)):
                for j in range(m):
                    if partition_upper_hulls[i][j].x < p:
                        del partition_upper_hulls[i][j]







    n = len(points)
    for i in range(log(log(n))):
        if (upper_hall_with_size(points,2**(2**i))):
            break            

            


            
def compute_tanget(point,points):

    tangent = "dummy"
    return tangent
        


    
