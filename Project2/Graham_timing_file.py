import time
import numpy as np
import matplotlib.pyplot as plt

from Orientation import orientation
from Shared import Point, sort_by_x_coordinate
from Generate_data import gen_circle_data, gen_square_data, gen_curve_data, make_points_from_numpy


def grahams_scan(points) -> list:
    
    # more than 2 points required for upper hull
    n = len(points)
    if n <= 2:
        return []

    upper_hull = []


    sort_start = time.time()

    #sort by x-coordinate and append 2 lowest points to upper hall
    sort_by_x_coordinate(points)

    global sort_time
    sort_time = (time.time() - sort_start)

    upper_hull.append(points[0])
    upper_hull.append(points[1])


    for i in range (2, n):

        # loop through the sorted points and add them to upper hull,
        # if orientation through last 2 points and current point doesn't make a right turn
        while len(upper_hull) >= 2 and orientation(upper_hull[len(upper_hull)-2], 
                                                   upper_hull[len(upper_hull)-1],
                                                   points[i]) != 1:
            del upper_hull[len(upper_hull)-1]
        upper_hull.append(points[i])

    return upper_hull

def plot_graham_running_times():
    xpoints = np.array(0.0,dtype=np.float64)
    sort_times = np.array(0.0,dtype=np.float64)
    total_times = np.array(0.0,dtype=np.float64)

    s = 8

    for i in range(2, 23):

        n = 2 ** i
        s = 1.4142*s

        x, y = gen_square_data(n,0,s)
        graham_points = make_points_from_numpy(n,x,y)

        xpoints = np.append(xpoints , n)

        total_start = time.time()
        graham = grahams_scan(graham_points)
        total_time = time.time() - total_start

        sort_times = np.append(sort_times, sort_time)
        total_times = np.append( total_times , total_time)

    plt.plot(xpoints, sort_times/total_times , label = "Sort time")
   # plt.plot(xpoints , total_times , label = "Total time")
    leg = plt.legend(loc='upper center')
    plt.ylabel("sort time/total time")
    plt.xlabel("input size")
   # plt.yscale('log',base=2)
    plt.xscale('log',base=2)
    plt.show()

plot_graham_running_times()