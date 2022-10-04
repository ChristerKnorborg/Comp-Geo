from copy import deepcopy
import matplotlib.pyplot as plt
import numpy as np
from Graham_scan import grahams_scan
from Gift_wrapping import gift_wrapping
from Shared import Point, print_points
from Chan_algorithm import chan_algorithm



def square_test(num_of_points, range_lower, range_upper):
    

    x = np.random.randint(range_lower,range_upper,num_of_points)
    y = np.random.randint(range_lower,range_upper,num_of_points)

    graham_points = []
    for i in range(num_of_points):
        p = Point(x[i],y[i])
        graham_points.append(p)
        del p

    gift_points = deepcopy(graham_points)
    chan_points = deepcopy(graham_points)


    graham_upper_hull = grahams_scan(graham_points)
    gift_upper_hull = gift_wrapping(gift_points)
    chan_upper_hull = chan_algorithm(chan_points)



    #print_points(upper_hull)

    graham_a = []
    graham_b = []
    for i in range(len(graham_upper_hull)):
        graham_a.append(graham_upper_hull[i].x)
        graham_b.append(graham_upper_hull[i].y)

    gift_a = []
    gift_b = []
    for i in range(len(gift_upper_hull)):
        gift_a.append(gift_upper_hull[i].x)
        gift_b.append(gift_upper_hull[i].y)    

    chan_a = []
    chan_b = []
    for i in range(len(chan_upper_hull)):
        chan_a.append(chan_upper_hull[i].x)
        chan_b.append(chan_upper_hull[i].y)          

    

    fig = plt.figure()

    ax1 = fig.add_subplot(131)
    ax2 = fig.add_subplot(132)
    ax3 = fig.add_subplot(133)
    #ax4 = fig.add_subplot(222)

    ax1.scatter(x,y)
    ax2.scatter(x,y)
    ax3.scatter(x,y)
    #ax4.scatter(x,y)
    


        

    #plt.scatter(x,y) 
    ax1.plot(graham_a, graham_b, color='red', linestyle='dashed', marker='o')
    ax2.plot(gift_a, gift_b, color='red', linestyle='dashed', marker='o')
    ax3.plot(chan_a, chan_b, color='red', linestyle='dashed', marker='o')

    ax1.set_title('Graham_scan')
    ax2.set_title('Gift_wrapping')
    ax3.set_title('Chan\'s_algorithm')

    plt.show()



def circle_test(num_of_points, diameter):


   # np.random.seed(1)
    theta = np.random.uniform(0,2*np.pi, num_of_points)
    diameter = np.random.uniform(0,diameter, num_of_points) ** 0.5

    x = diameter * np.cos(theta)
    y = diameter * np.sin(theta)

    graham_points = []
    for i in range(num_of_points):
        p = Point(x[i],y[i])
        graham_points.append(p)
        del p

    gift_points = deepcopy(graham_points)
    chan_points = deepcopy(graham_points)


    graham_upper_hull = grahams_scan(graham_points)
    gift_upper_hull = gift_wrapping(gift_points)
    chan_upper_hull = chan_algorithm(chan_points)



    #print_points(upper_hull)

    graham_a = []
    graham_b = []
    for i in range(len(graham_upper_hull)):
        graham_a.append(graham_upper_hull[i].x)
        graham_b.append(graham_upper_hull[i].y)

    gift_a = []
    gift_b = []
    for i in range(len(gift_upper_hull)):
        gift_a.append(gift_upper_hull[i].x)
        gift_b.append(gift_upper_hull[i].y)    

    chan_a = []
    chan_b = []
    for i in range(len(chan_upper_hull)):
        chan_a.append(chan_upper_hull[i].x)
        chan_b.append(chan_upper_hull[i].y)          

    

    fig = plt.figure()

    ax1 = fig.add_subplot(131)
    ax2 = fig.add_subplot(132)
    ax3 = fig.add_subplot(133)
    #ax4 = fig.add_subplot(222)

    ax1.scatter(x,y)
    ax2.scatter(x,y)
    ax3.scatter(x,y)
    #ax4.scatter(x,y)
    


        

    #plt.scatter(x,y) 
    ax1.plot(graham_a, graham_b, color='red', linestyle='dashed', marker='o')
    ax2.plot(gift_a, gift_b, color='red', linestyle='dashed', marker='o')
    ax3.plot(chan_a, chan_b, color='red', linestyle='dashed', marker='o')

    ax1.set_title('Graham_scan')
    ax2.set_title('Gift_wrapping')
    ax3.set_title('Chan\'s_algorithm')

    plt.show()





def curve_test(num_of_points, range_lower, range_upper):

    x = np.random.randint(range_lower,range_upper,num_of_points)
    y = -x**2


    graham_points = []
    for i in range(num_of_points):
        p = Point(x[i],y[i])
        graham_points.append(p)
        del p

    gift_points = deepcopy(graham_points)
    chan_points = deepcopy(graham_points)


    graham_upper_hull = grahams_scan(graham_points)
    gift_upper_hull = gift_wrapping(gift_points)
    chan_upper_hull = chan_algorithm(chan_points)



    #print_points(upper_hull)

    graham_a = []
    graham_b = []
    for i in range(len(graham_upper_hull)):
        graham_a.append(graham_upper_hull[i].x)
        graham_b.append(graham_upper_hull[i].y)

    gift_a = []
    gift_b = []
    for i in range(len(gift_upper_hull)):
        gift_a.append(gift_upper_hull[i].x)
        gift_b.append(gift_upper_hull[i].y)    

    chan_a = []
    chan_b = []
    for i in range(len(chan_upper_hull)):
        chan_a.append(chan_upper_hull[i].x)
        chan_b.append(chan_upper_hull[i].y)          

    

    fig = plt.figure()

    ax1 = fig.add_subplot(131)
    ax2 = fig.add_subplot(132)
    ax3 = fig.add_subplot(133)
    #ax4 = fig.add_subplot(222)

    ax1.scatter(x,y)
    ax2.scatter(x,y)
    ax3.scatter(x,y)
    #ax4.scatter(x,y)
    
    #plt.scatter(x,y) 
    ax1.plot(graham_a, graham_b, color='red', linestyle='dashed', marker='o')
    ax2.plot(gift_a, gift_b, color='red', linestyle='dashed', marker='o')
    ax3.plot(chan_a, chan_b, color='red', linestyle='dashed', marker='o')

    ax1.set_title('Graham_scan')
    ax2.set_title('Gift_wrapping')
    ax3.set_title('Chan\'s_algorithm')

    plt.show()



#square_test(100,0,5000)
circle_test(200,20000)
#curve_test(20,0,50)


