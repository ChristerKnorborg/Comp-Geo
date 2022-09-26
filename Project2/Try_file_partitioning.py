from math import floor
from turtle import left
from Gift_wrapping import gift_wrapping
from Shared import Point

p1 = 1
p2 = 2
p3 = 3
p4 = 4
p5 = 5
p6 = 6
p7 = 7
p8 = 8
p9 = 9
p10 = 10
p11 = 11

test_list = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p11]


h = 4

def divide_chunks(list, step) -> list:
    
    new_list = []

    if step > len(list):
        new_list.append(list)
        return new_list
        
    leftover_iterations = len(list) % step
    main_iterations = len(list) - leftover_iterations

    print("main iterations & leftover", main_iterations, leftover_iterations)

    for i in range(0, main_iterations, step):
        new_list.append(list[i:i+step])


    n = len(new_list)
    for i in range(0, leftover_iterations):
        add_idx = i % n
        print("iteration",i)
        new_list[add_idx].append(list[main_iterations+i])      

    return new_list
    


x = divide_chunks(test_list, h)
print(x)

