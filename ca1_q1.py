# date : 31/03/2021
# Author : Renato Gusani
# Student no. : x19411076
# Question - Q1.1 + Q1.2

# * * * * * * * * * * question 1.1) * * * * * * * * * *


# Constant Time — O(1) - first item in list; is list even or odd
def get_first(data):
    return data[0]
    
if __name__ == '__main__':
    data = [1, 2, 9, 8, 3, 4, 7, 6, 5]
    print(get_first(data))

# Logarithmic Time — O(log n) - binary search
for index in range(0, len(data), 3):
    print(data[index])


# Linear Time — O(n) - search linearly through list; print every item in list
for value in data:
    print(value)


# Quasilinear Time — O(n log n) - mergesort; quick sort
for value in data1:
    result.append(binary_search(data2, value))


# Quadratic Time/polynomial — O(n²) - loop nested within loop; bubble sort
for x in data:
    for y in data:
        print(x, y)


# Exponential Time — O(2^n) - count combinations of list elements
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


# Factorial — O(n!) - generate all permutations of a list
def heap_permutation(data, n):
    if n == 1:
        print(data)
        return
    
    for i in range(n):
        heap_permutation(data, n - 1)
        if n % 2 == 0:
            data[i], data[n-1] = data[n-1], data[i]
        else:
            data[0], data[n-1] = data[n-1], data[0]
    
if __name__ == '__main__':
    data = [1, 2, 3]
    heap_permutation(data, len(data))s




# * * * * * * * * * * question 1.2) * * * * * * * * * *

# * * This question has been answered on the word document * *





