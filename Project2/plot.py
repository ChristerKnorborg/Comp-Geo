from re import S
import numpy as np
import matplotlib.pyplot as plt
import time
from Chan_algorithm import chan_algorithm
from Gift_wrapping import gift_wrapping
from Graham_scan import grahams_scan
from Shared import Point


def generate_square_points_test(num_of_points, range_lower, range_upper):
    x = np.random.randint(range_lower,range_upper,num_of_points)
    y = np.random.randint(range_lower,range_upper,num_of_points)

    points = []
    for i in range(num_of_points):
        p = Point(x[i],y[i])
        points.append(p)
        del p

    return points

def generate_circle_points_test(num_of_points):
    # np.random.seed(1)
    theta = np.random.uniform(0,2*np.pi, num_of_points)
    diameter = np.random.uniform(0,diameter, num_of_points) ** 0.5

    x = diameter * np.cos(theta)
    y = diameter * np.sin(theta)

    points = []
    for i in range(num_of_points):
        p = Point(x[i],y[i])
        points.append(p)
        del p

    return points 


def bænkemærke_box():

    np.random.seed(100)

    xpoints = np.array(0.0,dtype=np.float64)
    grahamtimes = np.array(0.0 , dtype = np.float64)
    gifttimes = np.array(0.0,dtype = np.float64)
    chantimes = np.array(0.0,dtype = np.float64)


    s = 8
    for i in range(2, 16):
        print("Round: " , i)
        n = 2 ** i

        s = 1.41*s
        

        xpoints = np.append(xpoints , n)
        points = generate_square_points_test(n, 0, s)

        timestart_graham = time.time()
        graham = grahams_scan(points)
        timestop_graham = time.time()
        running_time_bland = timestop_graham - timestart_graham

        grahamtimes = np.append( grahamtimes , running_time_bland)
        print("Running time Graham Scan: " + str(running_time_bland))

        timestart_gift = time.time()
        gift = gift_wrapping(points)
        timestop_gift = time.time()
        running_time_coef = timestop_gift - timestart_gift

        gifttimes = np.append(gifttimes , running_time_coef)
        print("Running time Gift Wrapping: " + str(running_time_coef))


        timestart_chan = time.time()
        chan = chan_algorithm(points)
        timestop_chan = time.time()
        running_time_inc = timestop_chan - timestart_chan

        chantimes = np.append(chantimes , running_time_inc)
        print("Running time Chan: " + str(running_time_inc))

        chan_len = len(chan)
        gift_len = len(gift)
        graham_len = len(graham)

        lower_bound = graham_len * 0.9
        upper_bound = graham_len * 1.1

        if gift_len < lower_bound or gift_len > upper_bound:
            print("gift len over 10% away from graham")

        if chan_len < lower_bound or chan_len > upper_bound:
            print("chan len over 10% away from graham")

        

    plt.plot(xpoints ,  grahamtimes , label = "Graham Scan" )
    plt.plot(xpoints, gifttimes , label = "Gift Wrapping")
    plt.plot(xpoints , chantimes , label = "Chan's Algorithm")
    leg = plt.legend(loc='upper center')
    plt.show()


bænkemærke_box()