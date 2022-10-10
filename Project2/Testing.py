from copy import deepcopy
import matplotlib.pyplot as plt

from Shared import Point
from Graham_scan import grahams_scan
from Gift_wrapping import gift_wrapping
from Chan_algorithm import chan_algorithm
from Generate_data import gen_square_data, gen_circle_data, gen_curve_data, gen_negative_curve_data, make_points_from_numpy





def run_and_plot(num_of_points,x,y):

    graham_points = make_points_from_numpy(num_of_points,x,y)
    gift_points = deepcopy(graham_points)
    chan_points = deepcopy(graham_points)


    graham_upper_hull = grahams_scan(graham_points)
    gift_upper_hull = gift_wrapping(gift_points)
    chan_upper_hull = chan_algorithm(chan_points)


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

    ax1.scatter(x,y)
    ax2.scatter(x,y)
    ax3.scatter(x,y)

    ax1.plot(graham_a, graham_b, color='red', linestyle='dashed', marker='o')
    ax2.plot(gift_a, gift_b, color='red', linestyle='dashed', marker='o')
    ax3.plot(chan_a, chan_b, color='red', linestyle='dashed', marker='o')

    ax1.set_title('Graham_scan')
    ax2.set_title('Gift_wrapping')
    ax3.set_title('Chan\'s_algorithm')

    plt.show()





def square_test(num_of_points, range_lower, range_upper):

    x, y = gen_square_data(num_of_points, range_lower, range_upper)
    run_and_plot(num_of_points,x,y)



def circle_test(num_of_points, diameter_squared):

    x, y = gen_circle_data(num_of_points, diameter_squared)
    run_and_plot(num_of_points,x,y)



def curve_test(num_of_points, range_lower, range_upper):
    x, y = gen_curve_data(num_of_points, range_lower, range_upper)
    run_and_plot(num_of_points,x,y)


def negative_curve_test(num_of_points, range_lower, range_upper):
    x, y = gen_negative_curve_data(num_of_points, range_lower, range_upper)
    run_and_plot(num_of_points,x,y)


#square_test(150,0,50)
circle_test(2000,2000000)
#curve_test(20,0,50)
#negative_curve_test(20,0,50)

