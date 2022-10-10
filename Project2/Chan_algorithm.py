from math import ceil, log2
from re import L
from tabnanny import check
import time

from Graham_scan import grahams_scan
from Orientation import orientation
from Shared import Point
from Shared import get_leftmost_point_idx, get_rightmost_point_idx, divide_chunks

# find upper hull for a list of partitions.
# returns a list of upper hulls
def calc_partition_upper_hulls(partition):
    partition_upper_hulls = []
    for i in range(len(partition)):
       current_upper_hull = grahams_scan(partition[i])
       if current_upper_hull != None:
            partition_upper_hulls.append(current_upper_hull)
    return partition_upper_hulls



# find best tangent for a point p and an array of points arr,
# by using orientation for binary search
def binary_search_orientation(arr, p):
    
    low = 0
    high = len(arr)
    
    # If only 1 element, return this. If p is included in this upper_hull,
    # we simply return next element as this is the best tangent from graham.
    if len(arr) == 1:
        return arr[0]
    if p == arr[0]:
        return arr[1]

    while True:

        # calculate current element to check 
        mid = (low + high) // 2
        
        # Out of bounds check predecessor (to mid). If out of bounds percieve as right turn
        if mid != 0:
            predecessor = orientation(p, arr[mid], arr[mid-1])
        else:
            predecessor = 1

        # Out of bounds check successor (to mid). If out of bounds percieve as right turn
        if mid != len(arr)-1: 
            successor   = orientation(p, arr[mid], arr[mid+1])
        else:
            successor = 1
        
        # if predecessor left turn, limit search space to lower half
        if predecessor == 2:
            high = mid - 1

        # If successor right turn, limit search space to upper half.
        # Same applies if neither predecessor OR successor left turn. But successor is straight.
        # Here we only want to include the last point on a straight line on the upper hull.
        elif successor == 2 or successor == 0:
            low = mid + 1

        # if both neighbour test right turn or only predecessor is straight, we return index
        else:
            return arr[mid]








def upper_hall_with_size(points,h):
        #chunks_start = time.time()
        # Make m partitions
        partition = divide_chunks(points, h)
        #global chunks_time
        #chunks_time = (time.time() - chunks_start)


        # find upper hull for all m partitions
        #partition_start = time.time()
        partition_upper_hulls = calc_partition_upper_hulls(partition)

        #global partition_time
        #partition_time = (time.time() - partition_start)

        # Find start point p and max coordinate (stop criteria) 
        start_coordinate = get_leftmost_point_idx(points)
        max_coordinate = get_rightmost_point_idx(points)

        p = points[start_coordinate]
        max_coordinate_point = points[max_coordinate]

        upper_hull = []

        for i in range(h):

            upper_hull.append(p)


            # Upper_Hall computed if max coordinate is p
            if p == max_coordinate_point:
                return True, upper_hull


            best_tangent = None


            for j in range(len(partition_upper_hulls)):
                
                # check if upper hull exist for partition
                if len(partition_upper_hulls[j]) < 1:
                    continue

                else: 
                    new_tangent = binary_search_orientation(partition_upper_hulls[j], p)

                    if new_tangent != None:
                        if best_tangent == None:
                            best_tangent = new_tangent
                        else:
                            if orientation(p, best_tangent, new_tangent) == 2:
                                best_tangent = new_tangent
                            elif orientation(p, best_tangent, new_tangent) == 0 and new_tangent.x > best_tangent.x:
                                best_tangent = new_tangent

            

            if best_tangent != None:
                p = best_tangent
            #tangent_start = time.time()

            #global tangent_time
            #tangent_time = (time.time() - tangent_start)


            
            
            #remove_start = time.time()
            partition_upper_hulls = [[point for point in outer if point.x >= best_tangent.x] for outer in partition_upper_hulls]
            #global remove_time
            #remove_time = (time.time() - remove_start)

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

    print("CHAN DIDNT FIND UPPER HULL")            


#start_total = time.time()
#upper_hull = chan_algorithm(points)
#total_time = time.time() - start_total

#print("Total time: ", total_time)
#print("Tangent time: ", tangent_time)
#print("Partition time: ", partition_time)
#print("Chunks time: ", chunks_time)
#print("Remove time: ", remove_time)


#upper_hull = chan_algorithm(points)
#print(upper_hull)



