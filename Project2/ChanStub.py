from math import ceil, log2
from os import remove
from re import L
import time
import numpy as np
import matplotlib.pyplot as plt

from Graham_scan import grahams_scan
from Orientation import orientation
from Shared import Point, get_leftmost_point_idx, get_rightmost_point_idx
from Generate_data import gen_square_data, make_points_from_numpy


chunks_total = 0
graham_total = 0
tangent_total = 0
remove_total = 0

# partition a list into length of list / partitions_size (n/h). 
def partition_list(list, partitions_size) -> list:

    # if whole list fits into specified size of partitions, return the list in a list (with a single list inside).
    if partitions_size > len(list):
        return [list]

    new_list = []

    # calculate what to do with leftover elements that do not take up a whole partition
    leftover_iterations = len(list) % partitions_size
    main_iterations = len(list) - leftover_iterations
     
    # fill up as many whole partitions as possible
    for i in range(0, main_iterations, partitions_size):

        new_list.append(list[i:i+partitions_size])


    # If leftover elements are 3 or more, make a smaller partition with these (else case).
    # If leftover elements are less than 3, graham_scan does not work on such a partition.
    # Therefore, the first leftover element is put into the first partition, where the next
    # (if it exist) is put into the second partition.
    if leftover_iterations < 3 and leftover_iterations != 0:

        new_list[0].append(list[main_iterations])

        if leftover_iterations > 1:
        
            new_list[1].append(list[main_iterations+1])

    else:  
        
        new_list.append(list[main_iterations : main_iterations + leftover_iterations])


    return new_list


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


        chunks_start = time.time()

        # Make m partitions
        partitions = partition_list(points, h)
        chunks_time = (time.time() - chunks_start)
        global chunks_total
        chunks_total = chunks_total + chunks_time

        graham_start = time.time()
        
        # find upper hull for all m partitions
        partition_upper_hulls = calc_partition_upper_hulls(partitions)


        graham_time = (time.time() - graham_start)
        global graham_total
        graham_total = graham_total + graham_time

        # Find start point p and max coordinate end_point
        start_coordinate = get_leftmost_point_idx(points)
        max_coordinate = get_rightmost_point_idx(points)

        p = points[start_coordinate]
        end_point = points[max_coordinate]

        upper_hull = []
        for _ in range(h):

            upper_hull.append(p)


            # Upper_Hall computed if max coordinate is p
            if p == end_point:
                return True, upper_hull


            best_tangent = None


                # Find the tangent (new_tangent) to every partition of upper hulls.
                # Update the best tangent to the best of the tangents to the partitions.
            tangent_start = time.time()
            for i in range(len(partition_upper_hulls)):
                
                # check if upper hull exist for partition
                if len(partition_upper_hulls[i]) < 1:
                    continue

                else: 
                    new_tangent = binary_search_orientation(partition_upper_hulls[i], p)
                    
                    if best_tangent == None:
                        best_tangent = new_tangent
                    else:
                        # Update best tangent orientation through the best tangent to the new tangent makes a left turn
                        if orientation(p, best_tangent, new_tangent) != 1:
                            best_tangent = new_tangent

            
            p = best_tangent
            

            tangent_time = (time.time() - tangent_start)
            global tangent_total
            tangent_total = tangent_total + tangent_time
            
            
            remove_start = time.time()

            # Remove points from all partition_upper_hulls if their x-coordinate are lower than the new p.
            partition_upper_hulls = [[point for point in outer if point.x >= p.x] for outer in partition_upper_hulls]
            
            
            remove_time = (time.time() - remove_start)
            global remove_total
            remove_total = remove_total + remove_time

        
        return False, []


def chan_algorithm(points):

    # more than 2 points required for upper hull
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




def plot_chan_running_times():
    xpoints = np.array(0.0,dtype=np.float64)
    partition_times = np.array(0.0,dtype=np.float64)
    graham_times = np.array(0.0,dtype=np.float64)
    binary_times = np.array(0.0,dtype=np.float64)
    remove_times = np.array(0.0,dtype=np.float64)
    total_times = np.array(0.0,dtype=np.float64)

    s = 8

    for i in range(2, 19):

        n = 2 ** i
        s = 1.4142*s

        x, y = gen_square_data(n,0,s)

        start_total = time.time()
        chans_points = make_points_from_numpy(n,x,y)
        total_time = time.time() - start_total

        xpoints = np.append(xpoints , n)

        total_start = time.time()
        _ = chan_algorithm(chans_points)
        total_time = time.time() - total_start

        global chunks_total
        global graham_total
        global tangent_total
        global remove_total
        partition_times = np.append(partition_times, chunks_total)
        graham_times = np.append(graham_times, graham_total)
        total_times = np.append( total_times , total_time)
        binary_times = np.append (binary_times, tangent_total)
        remove_times = np.append(remove_times, remove_total)

        chunks_total = 0
        graham_total = 0
        tangent_total = 0
        remove_total = 0


    #partition_times = partition_times/total_times
    #graham_times = graham_times/total_times
    #binary_times = binary_times/total_times
    #remove_times = remove_times/total_times


    plt.plot(xpoints, partition_times , label = "Partition time")
    plt.plot(xpoints, graham_times , label = "Graham time")
    plt.plot(xpoints, binary_times , label = "Tangent time")
    plt.plot(xpoints, remove_times , label = "Remove time")
    plt.plot(xpoints , total_times , label = "Total time")
    leg = plt.legend(loc='upper center')
    plt.xscale('log', base=2)
    plt.show()


plot_chan_running_times()