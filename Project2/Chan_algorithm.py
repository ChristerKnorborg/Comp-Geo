from math import ceil, log2

from Graham_scan import grahams_scan
from Orientation import orientation
from Shared import get_leftmost_point_idx, get_rightmost_point_idx, divide_list_into_chunks, print_points, Point


def chan_algorithm(points):

    def upper_hall_with_size(points,h):
        
        n = len(points)
        m = ceil(n/h)

        print("h",h,"n",n,"m",m)

        # Make m partitions
        partition = list(divide_list_into_chunks(points, h))
        
        if len(partition) != m: 
            print("ERROR: PARTITION AND M DIFFERENT SIZE")
            return

        # find upper hull for all m partitions
        partition_upper_hulls = []
        for i in range(len(partition)):
            partition_upper_hulls.append(grahams_scan(partition[i]))

        if len(partition_upper_hulls) != m: 
            print("ERROR: partition_upper_hulls AND M DIFFERENT SIZE")    
            return


        upper_hull = []

        p = get_leftmost_point_idx(points)
        max_coordinate = get_rightmost_point_idx(points)

        point_p = points[p]
        max_coordinate_point = points[max_coordinate]

        for i in range(h):

            upper_hull.append(p)

            # Upper_Hall computed if max coordinate is point_p
            if point_p == max_coordinate_point:
                print("MAX COORDINATE BREAK: SUCCES!")
                break


            tanget_points = []
            print("LOOP", i, "partition_upper_hulls")            
            print(len(partition_upper_hulls))
            print(type(partition_upper_hulls))
            print(type(partition_upper_hulls[0]))
            print(len(partition_upper_hulls[0]))

            for j in range(len(partition_upper_hulls)):
                print("iteration", j, "len" , len(partition_upper_hulls[j]))
                print(type(partition_upper_hulls[j]))
                # Check if upper hall exist for partition. Otherwise continue to next upper hall partition.
                if len(partition_upper_hulls[j]) > 0:
                    best = partition_upper_hulls[j][0]
                else:
                    continue
                
                for k in range(len(partition_upper_hulls[j])):
                    if orientation(point_p, best, partition_upper_hulls[j][k]) == 2:
                        best = partition_upper_hulls[j][k]
                tanget_points.append(best)

            print("TANGET_POINTS")            
            print(len(tanget_points))
            print(type(tanget_points))
            print(type(tanget_points[0]))
            best = tanget_points[0]
            for k in range(len(tanget_points)):
                if orientation(point_p, best, tanget_points[k]) == 2:
                    best = tanget_points[k]
            
            point_p = best
            
                
            #for j in range(len(partition_upper_hulls)):
             #   partition_upper_hulls[j] = [point for point in partition_upper_hulls if point.x < best.x]


                #for k in range(len(partition_upper_hulls[j])):
                    
                 #   if partition_upper_hulls[j][k].x < best.x:


        print("FAILURE")



    n = len(points)
    
    range_param = ceil(log2(log2((n))))
    for i in range(1,range_param):
        h = ceil(2**(2**i))
        if (upper_hall_with_size(points,h)):
            break            


            

# Test grahams_scan
p1 = Point(1, 1)
p2 = Point(1, 2)
p3 = Point(2, 3)
p4 = Point(4, 3)
p5 = Point(4, 4)
p6 = Point(6, 2)
p7 = Point(6, 4)
p8 = Point(7, 3)
p9 = Point(8, 2)

test_list = [p1,p2,p3,p4,p5,p6,p7,p8,p9]

upper_hull = chan_algorithm(test_list)
print_points(upper_hull)
            


    
