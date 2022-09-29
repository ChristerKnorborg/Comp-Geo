from math import ceil, floor, log2

from Graham_scan import grahams_scan
from Orientation import orientation
from Shared import get_leftmost_point_idx, get_rightmost_point_idx, divide_chunks, print_points, Point


def chan_algorithm(points):

    def upper_hall_with_size(points,h):
        
        n = len(points)

        print("h",h,"n",n)

        # Make m partitions
        partition = divide_chunks(points, h)


        # find upper hull for all m partitions
        partition_upper_hulls = []

        for i in range(len(partition)):
            current_upper_hull = grahams_scan(partition[i])
            if current_upper_hull != None:
                partition_upper_hulls.append(current_upper_hull)


        upper_hull = []

        p = get_leftmost_point_idx(points)
        max_coordinate = get_rightmost_point_idx(points)

        point_p = points[p]
        max_coordinate_point = points[max_coordinate]


        for i in range(h):

            upper_hull.append(point_p)

            # Upper_Hall computed if max coordinate is point_p
            if point_p == max_coordinate_point:
                return True, upper_hull


            tanget_points = []


            for j in range(len(partition_upper_hulls)):
                # Check if upper hall exist for partition. Otherwise continue to next upper hall partition.
                if len(partition_upper_hulls[j]) > 0:
                    best = partition_upper_hulls[j][0]
                else:
                    continue
                
                for k in range(len(partition_upper_hulls[j])):
                    if orientation(point_p, best, partition_upper_hulls[j][k]) != 1:
                        best = partition_upper_hulls[j][k]
                    #else: del partition_upper_hulls[j][k]
                if best != None:
                    tanget_points.append(best)

            best = tanget_points[0]
            
            for k in range(len(tanget_points)):
                if orientation(point_p, best, tanget_points[k]) != 1:
                    best = tanget_points[k]
            if best != None:
                point_p = best
            
            partition_upper_hulls = [[point for point in outer if point.x >= best.x] for outer in partition_upper_hulls]


        return False, []




    n = len(points)
    if n <= 2:
        return
        
    range_param = ceil(log2(log2((n))))
    # from 1 to log log n. Range exclusive in python - why +1.
    for i in range(1,range_param+1):
        h = int(2**2**i)
        cond, upper_hull = upper_hall_with_size(points,h)
        if cond:
            return upper_hull            