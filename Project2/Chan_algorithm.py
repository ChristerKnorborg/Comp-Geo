from math import ceil, log2
import time
from tkinter import EW

from Graham_scan import grahams_scan
from Orientation import orientation
from Shared import get_leftmost_point_idx, get_rightmost_point_idx, divide_chunks, print_points, Point


tangent_time = 0
partition_time = 0


neighbour_left = arr[j][best_idx-1]
neighbour_right = arr[j][best_idx+1]

o_test_left = orientation(p,best,neighbour_left)
o_test_right = orientation(p,best,neighbour_right)

if o_test_left != 1:

def binary_search_orientation(arr, p):
    left = 0
    right = len(arr) - 1
 
    while low <= high:
 
        right = (left + right) // 2
 
        # If x is greater, ignore left half
        if orientation(p, arr[left], arr[right]):
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1



def binary_search(arr, low, high):

    for j in range(len(arr)):


        if len(arr[j]) > 0:
            best = arr[j][0]
            param = int(len(arr[j]) / 2)
            while (True):

                param_point = arr[j][param]

                o_test = orientation(p,best,param_point)                
                if o_test != 1:
                    best = arr[j][param]
                    best_idx = param
                    neighbour_left = arr[j][best_idx-1]
                    neighbour_right = arr[j][best_idx+1]

                    o_test_left = orientation(p,best,neighbour_left)
                    o_test_right = orientation(p,best,neighbour_right)
                    
                    if o_test_left != 1:
                        param = int(param/2)
                        print("havles")
                        if o_test_left == 0:
                            best 

                    elif o_test_right != 1:
                        param = int(param*1.5)
                        print("doubles")
                        
                    else: 
                        print("elso")
                        if best != None:
                            print("best is not none")
                            if best_tanget == None:
                                best_tanget = best
                            else:
                                if orientation(p, best_tanget, best) != 1:
                                    best_tanget = best
                        break
                    print(param)

                else:
                    continue



# find upper hull for all partitions
def calc_partition_upper_hulls(partition):
    partition_upper_hulls = []
    for i in range(len(partition)):
       current_upper_hull = grahams_scan(partition[i])
       if current_upper_hull != None:
            partition_upper_hulls.append(current_upper_hull)
    return partition


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

        for _ in range(h):

            upper_hull.append(p)

            # Upper_Hall computed if max coordinate is p
            if p == max_coordinate_point:
                return True, upper_hull


            best_tanget = None


            #tangent_start = time.time()


                

            '''
            # Check if upper hall exist for partition. Otherwise continue to next upper hall partition.
            if len(partition_upper_hulls[j]) > 0:
                # set best to lowest coordinate in the upper hull partition
                best = partition_upper_hulls[j][0]
            else:
                continue
            '''
            best_tanget = binary_search(partition_upper_hulls, 0, len(partition_upper_hulls)-1)

            #global tangent_time
            #tangent_time = (time.time() - tangent_start)

            #if best_tanget != None:
             #   p = best
            
            
            #remove_start = time.time()
            partition_upper_hulls = [[point for point in outer if point.x >= best.x] for outer in partition_upper_hulls]
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






points = []
for i in range(0,100):
    p = Point(i,i)
    points.append(p)


#start_total = time.time()
upper_hull = chan_algorithm(points)
#total_time = time.time() - start_total

#print("Total time: ", total_time)
#print("Tangent time: ", tangent_time)
#print("Partition time: ", partition_time)
#print("Chunks time: ", chunks_time)
#print("Remove time: ", remove_time)

print(upper_hull)





'''for j in range(len(partition_upper_hulls)):
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
'''