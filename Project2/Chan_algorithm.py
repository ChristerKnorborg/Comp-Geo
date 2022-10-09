from math import ceil, log2
import time

from Graham_scan import grahams_scan
from Orientation import orientation
from Shared import get_leftmost_point_idx, get_rightmost_point_idx, divide_chunks, print_points, Point

def printarray(arr):
    
    print("\nlen of arr:", len(arr))
    for p in arr:
        print((p.x,p.y))


def binary_search_orientation(arr, p):
    low = 0
    high = len(arr) - 1
    #printarray(arr)
    

    while low <= high:
        mid = (low + high) // 2

        # out of range check
        if mid != 0:
            predecessor = orientation(p, arr[mid], arr[mid-1])
        else: 
            predecessor = 1
        

        if mid != len(arr)-1:
            successor = orientation(p, arr[mid], arr[mid+1])
        else:
            successor = 1
        


        # If predecessor left turn and successor right turn, split in lower halves.
        if predecessor == 2:
            high = mid - 1

        # If predecessor right turn and successor left turn, split in upper halves.
        # Same applies if neither predecessor OR successor left turn. But successor is straight.
        # Here we want 
        elif successor == 2:
            low = mid + 1

        elif successor == 0:
            low = mid + 1

        # If neither predecessor OR successor left turn. But successor is straight
        #elif predecessor == 0:
            #high = mid -1

        else:
            return arr[mid]



    # If we reach here, then the element was not present
    print("Binary Search didn't find optimal")
    return None





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
                print("max coord")
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
                            if orientation(p, best_tangent, new_tangent) != 1:
                                best_tangent = new_tangent



                if best_tangent != None:
                    print("tangent:", (best_tangent.x,best_tangent.y))
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


p0 = Point(0,0)
p1 = Point(1,1)
p2 = Point(1,2)
p3 = Point(2,3)
p4 = Point(3,4)
p5 = Point(6,4)
p6 = Point(8,2)
p7 = Point(9,1)

points = [p0,p1,p2,p3,p4,p5,p6,p7]

'''
points = []
for i in range(0,10):
    ex = -(i ** 2)
    p = Point(i,ex)
    points.append(p)
    '''


tangent = binary_search_orientation(points,points[1])
print(tangent.x,tangent.y)

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



