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

def run_algorithm_square(algorithm, range_lower, range_upper, num_of_points):
    points = generate_square_points_test(range_lower, range_upper, num_of_points)

    upper_hull = algorithm(points)


def bænkemærke_box():

    np.random.seed(100)

    xpoints = np.array(0.0,dtype=np.float64)
    blandtimes = np.array(0.0 , dtype = np.float64)
    coeftimes = np.array(0.0,dtype = np.float64)
    inctimes = np.array(0.0,dtype = np.float64)

    for i in range(1, 40):
        print("Round: " , i)
        n = 2 ** i
        

        xpoints = np.append(xpoints , n)

        timestart_graham = time.time()
        run_algorithm_square(grahams_scan, n, 0, i*10)
        timestop_graham = time.time()
        running_time_bland = timestop_graham - timestart_graham

        blandtimes = np.append(blandtimes , running_time_bland)
        print("Running time Graham Scan: " + str(running_time_bland))

        timestart_gift = time.time()
        run_algorithm_square(gift_wrapping, n, 0, i*10)
        timestop_gift = time.time()
        running_time_coef = timestop_gift - timestart_gift

        coeftimes = np.append(coeftimes , running_time_coef)
        print("Running time Gift Wrapping: " + str(running_time_coef))


        timestart_chan = time.time()
        run_algorithm_square(chan_algorithm, i*10, 0, n)
        timestop_chan = time.time()
        running_time_inc = timestop_chan - timestart_chan

        inctimes = np.append(inctimes , running_time_inc)
        print("Running time Chan: " + str(running_time_inc))

    plt.plot(xpoints , blandtimes , label = "Graham Scan" )
    plt.plot(xpoints, coeftimes , label = "Gift Wrapping")
    plt.plot(xpoints , inctimes , label = "Chan's Algorithm")
    leg = plt.legend(loc='upper center')
    plt.show()


bænkemærke_box()