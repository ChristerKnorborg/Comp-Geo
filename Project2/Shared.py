class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    

def sort_by_x_coordinate(points):
    points.sort(key=lambda p: (p.x, p.y))

def get_leftmost_point_idx(points):
    min_idx = 0
    for idx, _ in enumerate(points):
        if points[idx].x < points[min_idx].x:
            min_idx = idx
        elif points[idx].x == points[min_idx].x:
            if points[idx].y < points[min_idx].y:
                min_idx = idx 
    return min_idx

def get_rightmost_point_idx(points):
    max_idx = 0
    for idx, p in enumerate(points):
        if points[idx].x > points[max_idx].x:
            max_idx = idx
        elif points[idx].x == points[max_idx].x:
            if points[idx].y > points[max_idx].y:
                max_idx = idx 

    return max_idx


def print_points(points):
    for p in points:
        print(p.x, p.y)


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




#tester =[p3, p1, p2]
#print("Før:")
#print_points(tester)
#sort_by_x_coordinate(tester)
#print("Efter:")
##print_points(tester)
##




















