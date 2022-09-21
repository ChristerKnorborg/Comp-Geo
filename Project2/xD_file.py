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
n = 3

def divide_chunks(list, chucks):
    for i in range(0, len(list), chucks):
        yield list[i:i + chucks]


x = list(divide_chunks(test_list, n))

print(x)
print("værdi?")
print(x[0][2].x)
print("len?")
print(len(x[0]))

print(len(test_list))


print(gift_wrapping(x[0]))