from math import ceil, floor, log2

from Graham_scan import grahams_scan
from Orientation import orientation
from Shared import get_leftmost_point_idx, get_rightmost_point_idx, divide_chunks, print_points, Point


def chan_algorithm(points):

    def upper_hall_with_size(points,h):
        
        n = len(points)
        m = floor(n/h)

        print("h",h,"n",n,"m",m)

        # Make m partitions
        partition = divide_chunks(points, h)


        # find upper hull for all m partitions
        partition_upper_hulls = []
        print("\n partition\n", partition)
        for i in range(len(partition)):
            current_upper_hull = grahams_scan(partition[i])
            if current_upper_hull != None:
                partition_upper_hulls.append(current_upper_hull)

        print("\n partition_upper_hulls\n", partition_upper_hulls)
        upper_hull = []

        p = get_leftmost_point_idx(points)
        max_coordinate = get_rightmost_point_idx(points)

        point_p = points[p]
        max_coordinate_point = points[max_coordinate]

        print("\n Leftmost point:\n" , point_p)

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
                if best != None:
                    tanget_points.append(best)

            print("\n TANGET_POINTS \n", tanget_points)
            best = tanget_points[0]
            for k in range(len(tanget_points)):
                if orientation(point_p, best, tanget_points[k]) != 1:
                    best = tanget_points[k]
            print("\n BEST TANGENT (x, y) \n", (best.x, best.y))
            if best != None:
                point_p = best
            
            
                
            for j in range(len(partition_upper_hulls)):
               for k in range(len(partition_upper_hulls[j])):
                    if partition_upper_hulls[j][k].x < best.x:
                        print("\n should remove point \n ", (partition_upper_hulls[j][k].x, partition_upper_hulls[j][k].y))


            # 
            partition_upper_hulls = [[point for point in outer if point.x >= best.x] for outer in partition_upper_hulls]
            print("\npartition_upper_hulls after remove \n", partition_upper_hulls)

        print("\n End of loop upper hull \n")
        for p in upper_hull:
            print(" ", (p.x,p.y))

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
            


    
