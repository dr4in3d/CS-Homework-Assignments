#Daniel Eke
#CS566 Analysis of Algorithms
#2/25/19

import sys
from timeit import default_timer as timer
import os
import math


def findmaxcross(input_array, low, mid, high):
    left_sum = float("-inf")
    current_sum = 0
    max_left = 0
    max_right = 0

    #low - 1 because we are passing index 1 in the main function instead of 0
    for i in range(mid, low - 1, -1): #mid downto low
        current_sum = current_sum + input_array[i]
        if current_sum > left_sum:
            left_sum = current_sum
            max_left = i
    right_sum = float("-inf")
    current_sum = 0
    for j in range(mid + 1, high):
        current_sum = current_sum + input_array[j]
        if current_sum > right_sum:
            right_sum = current_sum
            max_right = j
    return max_left, max_right, left_sum + right_sum


def divideandconquer(input_array, low, high):
    if high == low:
        return low, high, input_array[low - 1]

    else:
        mid = math.floor((low + high)/2)
        left_low, left_high, left_sum = divideandconquer(input_array, int(low), int(mid))
        right_low, right_high, right_sum = divideandconquer(input_array, int(mid+1), int(high))
        cross_low, cross_high, cross_sum = findmaxcross(input_array, int(low), int(mid), int(high))
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum

def main():
    #load the text file into an array

    input1 = sys.argv[1]
    file = open(input1)  # here is where you input the text file

    values = []
    for line in file:
        values.append(int(line))

    file.close()
    input_array = values
    n = len(values)
    #run divide and conquer
    start_time = timer()
    divideandconquer(input_array, 0, n)
    print(divideandconquer(input_array, 0, n))

    end_time = timer()
    elapsed_time = (end_time - start_time) * 1000 #converts to milliseconds
    print(elapsed_time)

if __name__ == '__main__':
    main()
