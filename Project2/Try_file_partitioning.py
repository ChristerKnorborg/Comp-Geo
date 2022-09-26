from math import floor
from turtle import left
from Gift_wrapping import gift_wrapping
from Shared import Point

p1 = Point(1, 1)
p2 = Point(1, 2)
p3 = Point(2, 3)
p4 = Point(4, 3)
p5 = Point(4, 4)
p6 = Point(6, 2)
p7 = Point(6, 4)
p8 = Point(7, 3)
p9 = Point(8, 2)

test_list = [p1,p2,p3,p4,p5,p6,p7,p8,p9]

start = 0
h = 4

def divide_chunks(list, step) -> list:

    new_list = []
    
    leftover_iterations = len(list) % step
    main_iterations = len(list) - leftover_iterations

    for i in range(0, main_iterations, step):
        new_list.append(list[i:i+step])

    for i in range(0, leftover_iterations):
        new_list[i].append(list[main_iterations+i])      

    return new_list
    


x = divide_chunks(test_list, h)
print(x)

