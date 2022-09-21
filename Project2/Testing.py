from nis import match
import matplotlib.pyplot as plt
import numpy as np
from Graham_scan import grahams_scan
from Gift_wrapping import gift_wrapping
from Shared import Point, print_points



def square_test(algorithm, num_of_points, range_lower, range_upper):
    

    x = np.random.randint(range_lower,range_upper,num_of_points)
    y = np.random.randint(range_lower,range_upper,num_of_points)



    points = []
    for i in range(num_of_points):
        p = Point(x[i],y[i])
        points.append(p)
        del p

    upper_hull = algorithm(points)



    print_points(upper_hull)

    a = []
    b = []
    for i in range(len(upper_hull)):
        a.append(upper_hull[i].x)
        b.append(upper_hull[i].y)
        

    plt.scatter(x,y) 
    plt.plot(a, b, color='red', linestyle='dashed', marker='o')
    plt.show()



def circle_test(algorithm, num_of_points, radius):


    np.random.seed(1)
    theta = np.random.uniform(0,2*np.pi, num_of_points)
    radius = np.random.uniform(0,radius, num_of_points)

    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    points = []
    for i in range(num_of_points):
        p = Point(x[i],y[i])
        points.append(p)
        del p

    upper_hull = algorithm(points)



    print_points(upper_hull)

    a = []
    b = []
    for i in range(len(upper_hull)):
        a.append(upper_hull[i].x)
        b.append(upper_hull[i].y)
        

    plt.scatter(x,y) 
    plt.plot(a, b, color='red', linestyle='dashed', marker='o')
    plt.show()





def curve_test(algorithm, num_of_points, range_lower, range_upper):

    x = np.random.randint(range_lower,range_upper,num_of_points)
    y = x**2


    points = []
    for i in range(num_of_points):
        p = Point(x[i],y[i])
        points.append(p)
        del p

    upper_hull = algorithm(points)



    print_points(upper_hull)

    a = []
    b = []
    for i in range(len(upper_hull)):
        a.append(upper_hull[i].x)
        b.append(upper_hull[i].y)
        

    plt.scatter(x,y) 
    plt.plot(a, b, color='red', linestyle='dashed', marker='o')
    plt.show()



curve_test(gift_wrapping,1000,0,50)
