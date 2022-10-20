# date is 10/19/22 and we're picking up algo's from yesterday, still working through basic 13

# Square the Values - sq each value in a give list, return the same list with changed values.

def square_list(li:list):
    for i in range(0, len(li)):
        li[i] = li[i] ** 2
    return li

# print(square_list([2,3,4]))

# Zero out negative numbers - return the given list, after setting any negative values to zero.

def zero_out(li:list[int]):
    for i in range(0, len(li)):
        if li[i] < 0:
            li[i] = 0
    return li

# print(zero_out([-1, 235, -25, 23, 5, 0]))

# Shift List Values - given a list, move all valuse forward by one index, dropping the first and leaving a '0' value at the end. 

def shift_list(li:list):
    for i  in range(1, len(li)):
        li[i-1] = li[i]
    li[-1] = 0 #python gives us the ability to loop backwards so this gives us the last index of a given list. 
    return li

print(shift_list([1,2,3,4,5]))