import matplotlib.pyplot as plt
import numpy as np
from Graham_scan import grahams_scan
from Gift_wrapping import gift_wrapping
from Shared import Point, print_points

num_of_points = 200

x = np.random.randint(0,100,num_of_points)
y = np.random.randint(0,100,num_of_points)



points = []
for i in range(num_of_points):
    p = Point(x[i],y[i])
    points.append(p)
    del p

upper_hull = grahams_scan(points)
print_points(upper_hull)

a = []
b = []
for i in range(len(upper_hull)):
    a.append(upper_hull[i].x)
    b.append(upper_hull[i].y)
    



plt.scatter(x,y) 
plt.plot(a, b, color='red', linestyle='dashed', marker='o')
plt.show()



