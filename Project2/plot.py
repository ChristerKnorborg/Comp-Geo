from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
import time
from Chan_algorithm import chan_algorithm
from Gift_wrapping import gift_wrapping
from Graham_scan import grahams_scan
from Generate_data import gen_circle_data, gen_square_data, gen_curve_data, make_points_from_numpy, gen_negative_curve_data
from enum import Enum

class test_type(Enum):
    square = 1
    circle = 2
    curve = 3
    neg_curve = 4

def benchmark_lin(test_type):
   # np.random.seed(100)

    xpoints = np.array(0.0,dtype=np.float64)
    grahamtimes = np.array(0.0 , dtype = np.float64)
    gifttimes = np.array(0.0,dtype = np.float64)
    chantimes = np.array(0.0,dtype = np.float64)

    n = 5000
    s = 50

    for i in range(1, 50):
        print("Round: " , i)

        n = n + 5000
        s = s + 50

        if test_type.square :
            x, y = gen_square_data(n,0,s)

        elif test_type.circle:
            x, y = gen_circle_data(n,s)

        elif test_type.curve:
            x, y = gen_curve_data(n,0,s)

        elif test_type.neg_curve:
            x, y = gen_negative_curve_data(n, 0, s)
        
        graham_points = make_points_from_numpy(n,x,y)
        gift_points = deepcopy(graham_points)
        chan_points = deepcopy(graham_points)

        xpoints = np.append(xpoints , n)


        timestart_graham = time.time()
        graham = grahams_scan(graham_points)
        timestop_graham = time.time()
        running_time_grham = timestop_graham - timestart_graham

        grahamtimes = np.append( grahamtimes , running_time_grham)
        #print("Running time Graham Scan: " + str(running_time_grham))

        timestart_gift = time.time()
        gift = gift_wrapping(gift_points)
        timestop_gift = time.time()
        running_time_gift = timestop_gift - timestart_gift

        gifttimes = np.append(gifttimes , running_time_gift)
        #print("Running time Gift Wrapping: " + str(running_time_gift))


        timestart_chan = time.time()
        chan = chan_algorithm(chan_points)
        timestop_chan = time.time()
        running_time_chan = timestop_chan - timestart_chan

        chantimes = np.append(chantimes , running_time_chan)
       # print("Running time Chan: " + str(running_time_chan))

    ''' #chan_len = len(chan)
        #gift_len = len(gift)
        #graham_len = len(graham)

        #lower_bound = graham_len * 0.75
        #upper_bound = graham_len * 1.25

        #if gift_len < lower_bound or gift_len > upper_bound:
            #print("gift len over 25% away from graham")

        #if chan_len < lower_bound or chan_len > upper_bound:
            #print("chan len over 25% away from graham") '''

        

    plt.scatter(xpoints ,  grahamtimes , c="blue" , label = "Graham Scan" )
    plt.scatter(xpoints, gifttimes, c="green", label = "Gift Wrapping")
    plt.scatter(xpoints , chantimes , c="red", label = "Chan's Algorithm")
    leg = plt.legend(loc='upper center')
    #plt.xscale('log',base=2)
    plt.show()

def benchmark(test_type):
   # np.random.seed(100)

    xpoints = np.array(0.0,dtype=np.float64)
    grahamtimes = np.array(0.0 , dtype = np.float64)
    gifttimes = np.array(0.0,dtype = np.float64)
    chantimes = np.array(0.0,dtype = np.float64)


    s = 8

    for i in range(2, 22):
        print("Round: " , i)

        # double number of points each test iteration and
        # double size of figure each iteration. Same 41.42% increase in both radius (circle) and a side in square

        n = 2 ** i
        s = 1.4142*s

        if test_type.square :
            x, y = gen_square_data(n,0,s)

        elif test_type.circle:
            x, y = gen_circle_data(n,s)

        elif test_type.curve:
            x, y = gen_curve_data(n,0,s)

        elif test_type.neg_curve:
            x, y = gen_negative_curve_data(n, 0, s)
        
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

    ''' #chan_len = len(chan)
        #gift_len = len(gift)
        #graham_len = len(graham)

        #lower_bound = graham_len * 0.75
        #upper_bound = graham_len * 1.25

        #if gift_len < lower_bound or gift_len > upper_bound:
            #print("gift len over 25% away from graham")

        #if chan_len < lower_bound or chan_len > upper_bound:
            #print("chan len over 25% away from graham") '''

        

    plt.plot(xpoints ,  grahamtimes/xpoints , label = "Graham Scan" )
    plt.plot(xpoints, gifttimes/xpoints , label = "Gift Wrapping")
    plt.plot(xpoints , chantimes/xpoints , label = "Chan's Algorithm")

    plt.ylabel("running time/input size")
    plt.xlabel("input size")

    leg = plt.legend(loc='upper center')
    plt.xscale('log',base=2)
    plt.show()


benchmark(test_type.neg_curve)