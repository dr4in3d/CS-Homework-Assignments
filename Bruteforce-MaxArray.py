#Daniel Eke
#CS566 Analysis of Algorithms
#2/25/19

import sys
from timeit import default_timer as timer
import os
import math
import array


#path = "C:/Users/dee1/documents/p1-data/random-2000.txt"

def bruteforce(input_array):
    n = len(input_array)
    maxsofar = float("-inf")

    for l in range (0, n):
        current_sum = 0
        for h in range(l,n):
            current_sum = current_sum + input_array[h]
            if current_sum > maxsofar:
                maxsofar = current_sum
                low = l
                high = h

                print(n, low, high, maxsofar)

#brute force test
def main():
    #load the text file into an array
    input1 = sys.argv[1]
    file = open(input1)  # here is where you input the text file

    values = []
    for line in file:
        values.append(int(line))

    file.close()
    input_array = values
    #run bruteforce
    start_time = timer()
    bruteforce(input_array)

    end_time = timer()
    elapsed_time = (end_time - start_time) * 1000 #converts to milliseconds
    print(elapsed_time)



main()









