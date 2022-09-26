from math import ceil, floor
from turtle import left
from Gift_wrapping import gift_wrapping
from Shared import Point






def divide_chunks(list, step) -> list:
    
    new_list = []

    if step > len(list):
        new_list.append(list)
        return new_list
        
    leftover_iterations = len(list) % step
    main_iterations = len(list) - leftover_iterations
     
    for i in range(0, main_iterations,step):
        new_list.append(list[i:i+step])


    # to make algorithm runable
    if leftover_iterations < 3 and leftover_iterations != 0:
        new_list[0].append(list[main_iterations])
        if leftover_iterations > 1:
            new_list[1].append(list[main_iterations+1])
    else:  
        new_list.append(list[main_iterations : main_iterations + leftover_iterations])

    return new_list
    

h = 4

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



test_list = [p1,p2,p3,p4,p5,p6,p7,p8,p9]

x = divide_chunks(test_list, h)
print(x)

