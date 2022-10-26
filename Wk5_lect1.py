"""
edabit.com/challenges -> website that lets you explore 
"""

# Sum of Odd and Evan Numbers
# write a function that takes a list of numbers and returns  a list with two elements. 
    # the first element should be the sum of all even numbers in the list. 
    # the second element should be the sum of all odd numbers in the list. 

# Define a function that accepts a list of integers
def even_and_odd(list:list[int]):
    # declare a results list (empty)
    results = [0, 0]
    # Loop through the given list 
    for num in list: 
        # if integer is even...
        if num % 2 == 0:
            # add integer to results[0]
            results[0] += num
        # else...
        else: 
            # add integer to results[1]
            results[1] += num
    # return results list 
    return results

print(even_and_odd([1, 2, 3, 4, 5, 6]))