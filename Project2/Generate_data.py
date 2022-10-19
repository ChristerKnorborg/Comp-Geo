import numpy as np
from Shared import Point


def gen_square_data(num_of_points, range_lower,range_upper):
    x = np.random.randint(range_lower,range_upper,num_of_points)
    y = np.random.randint(range_lower,range_upper,num_of_points)

    return x,y

def gen_circle_data(num_of_points, diameter):
    theta = np.random.uniform(0,2*np.pi, num_of_points)
    diameter = np.random.uniform(0,diameter, num_of_points) ** 0.5

    x = diameter * np.cos(theta)
    y = diameter * np.sin(theta)

    return x,y

def gen_positive_curve_data(num_of_points, range_lower, range_upper):
    x = np.random.randint(range_lower,range_upper,num_of_points)
    y = y = pow(x, 2) 

    return x,y


def gen_negative_curve_data(num_of_points, range_lower, range_upper):
    x = np.random.randint(range_lower,range_upper,num_of_points)
    y = pow(x, 2) 
    y = -y
    

    return x,y


def make_points_from_numpy(num_of_points,x,y):
    points = []
    for i in range(num_of_points):
        p = Point(x[i],y[i])
        points.append(p)
        del p
    return points