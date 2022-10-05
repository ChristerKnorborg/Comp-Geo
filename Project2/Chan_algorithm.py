from math import ceil, log2

from Graham_scan import grahams_scan
from Orientation import orientation
from Shared import get_leftmost_point_idx, get_rightmost_point_idx, divide_chunks, print_points, Point

# find upper hull for all partitions
def calc_partition_upper_hulls(partition):
    partition_upper_hulls = []
    for i in range(len(partition)):
       current_upper_hull = grahams_scan(partition[i])
       if current_upper_hull != None:
            partition_upper_hulls.append(current_upper_hull)
    return partition


def upper_hall_with_size(points,h):
        
        # Make m partitions
        partition = divide_chunks(points, h)

        # find upper hull for all m partitions
        partition_upper_hulls = calc_partition_upper_hulls(partition)

        # Find start point p and max coordinate (stop criteria) 
        start_coordinate = get_leftmost_point_idx(points)
        max_coordinate = get_rightmost_point_idx(points)

        p = points[start_coordinate]
        max_coordinate_point = points[max_coordinate]

        upper_hull = []

        for _ in range(h):

            upper_hull.append(p)

            # Upper_Hall computed if max coordinate is p
            if p == max_coordinate_point:
                return True, upper_hull


            best_tanget = None


            for j in range(len(partition_upper_hulls)):
                # Check if upper hall exist for partition. Otherwise continue to next upper hall partition.
                if len(partition_upper_hulls[j]) > 0:
                    best = partition_upper_hulls[j][0]
                else:
                    continue
                
                for k in range(len(partition_upper_hulls[j])):
                    if orientation(p, best, partition_upper_hulls[j][k]) != 1:
                        best = partition_upper_hulls[j][k]

                    #else: del partition_upper_hulls[j][k]
                if best != None:
                    if best_tanget == None:
                        best_tanget = best
                    else:
                        if orientation(p, best_tanget, best) != 1:
                            best_tanget = best
                        

            if best_tanget != None:
                p = best
            
            partition_upper_hulls = [[point for point in outer if point.x >= best.x] for outer in partition_upper_hulls]

        return False, []


def chan_algorithm(points):

    n = len(points)
    if n <= 2:
        return

    # from 1 to log log n. Range exclusive in python - why +1.    
    range_param = ceil(log2(log2((n)))) + 1
    for i in range(1,range_param):
        h = int(2**2**i)
        cond, upper_hull = upper_hall_with_size(points,h)
        if cond:
            return upper_hull            
