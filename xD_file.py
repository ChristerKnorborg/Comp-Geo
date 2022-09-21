my_list = [1, 2, 3, 4, 5,
           6, 7, 8, 9, 6, 7, 8, 9, 6, 7, 8, 9]
start = 0
end = 10
step = 3
for i in range(start, len(my_list), step):
    x = my_list[i:i+step]

    print(len(x))
    print(end/step)