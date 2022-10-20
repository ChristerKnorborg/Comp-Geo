from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
import time
from Chan_algorithm import chan_algorithm
from Gift_wrapping import gift_wrapping
from Graham_scan import grahams_scan
from Generate_data import gen_circle_data, gen_square_data, gen_positive_curve_data, make_points_from_numpy, gen_negative_curve_data
from enum import Enum


def benchmark(test_case):

    xpoints = np.empty(0,dtype=np.float64)
    grahamtimes = np.empty(0 , dtype = np.float64)
    gifttimes = np.empty(0,dtype = np.float64)
    chantimes = np.empty(0,dtype = np.float64)



    for i in range(2,18):
        print("Round: " , i)

        # double number of points each test iteration and

        n = pow(2, i)
        print("n:", n)
        

        if test_case == 1:
            x, y = gen_square_data(n,-10000,10000)

        elif test_case == 2:
            x, y = gen_circle_data(n,1000000)

        elif test_case == 3:
            x, y = gen_positive_curve_data(n,-1200,1200)

        elif test_case == 4:
            x, y = gen_negative_curve_data(n,-1200,1200)
        
        graham_points = make_points_from_numpy(n,x,y)
        gift_points = deepcopy(graham_points)
        chan_points = deepcopy(graham_points)

        xpoints = np.append(xpoints , n)


        timestart_graham = time.process_time()
        graham = grahams_scan(graham_points)
        timestop_graham = time.process_time()
        running_time_grham = timestop_graham - timestart_graham

        grahamtimes = np.append( grahamtimes , running_time_grham)
        #print("Running time Graham Scan: " + str(running_time_grham))

        timestart_gift = time.process_time()
        gift = gift_wrapping(gift_points)
        timestop_gift = time.process_time()
        running_time_gift = timestop_gift - timestart_gift

        gifttimes = np.append(gifttimes , running_time_gift)
        #print("Running time Gift Wrapping: " + str(running_time_gift))


        timestart_chan = time.process_time()
        chan = chan_algorithm(chan_points)
        timestop_chan = time.process_time()
        running_time_chan = timestop_chan - timestart_chan

        chantimes = np.append(chantimes , running_time_chan)
       # print("Running time Chan: " + str(running_time_chan))
        print("Graham, Gift, Chan:")    
        print(len(graham))
        print(len(gift))
        print(len(chan))



    print("graham times:")
    print(grahamtimes)
    print("gift times:")
    print(gifttimes)
    print("chan times:")
    print(chantimes)
    print("x points")
    print(xpoints)


        
    plt.plot(xpoints ,  grahamtimes*1000 , label = "Graham Scan" )
    plt.plot(xpoints, gifttimes*1000 , label = "Gift Wrapping")
    plt.plot(xpoints , chantimes*1000 , label = "Chan's Algorithm")

    plt.ylabel("running time/input size")
    plt.xlabel("input size")

    leg = plt.legend(loc='upper center')
    plt.xscale('log',base=2)
    #plt.yscale('log',base=2)
    plt.show()


# parameter: 1 = square, 2 = circle, 3 = positive_curve, 4 = negative_curve
benchmark(2)