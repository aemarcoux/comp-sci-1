# Author: Alexander Marcoux
# Date: 22 February 2023
# Purpose: Binary Search Recursive Algorithm
from random import *

# Perform binary search for key on the sublist of the_list
# starting at index left and going up to and including index right.
# If key appears in the_list, return the index where it appears.
# Otherwise, return None.
# Requires the_list to be sorted.

def binary_search(the_list, key, left = None, right = None):

    # If using the default parameters, then search the entire list.
        if left == None and right == None:
            left = 0
            right = len(the_list) - 1

        if left > right:
            return None

        if len(the_list) == 0:
            return None

        else:
            # the point from which you will look for value
            midpoint = (left + right) // 2

            # base case (initialize midpoint) and check if key is in list
            if the_list[midpoint] == key and key in the_list:
                return midpoint

            elif the_list[midpoint] < key:
                left = midpoint + 1

            else:  # the_list[midpoint] > key:
                right = midpoint - 1

            # returns the value passed from each call as you go back up from base case
            # if value is never found, will return None
            return binary_search(the_list, key, left, right)


# Driver code for binary search.
n = int(input("How many items in the list? "))

# Make a list of n random ints.
i = 0
the_list = []
while i < n:
    the_list.append(randint(0, 1000))
    i += 1

# Binary search wants a sorted list.
the_list = sorted(the_list)
print("The list: " + str(the_list))

while True:
    key = input("What value to search for? ('?' to see the list, 'q' to quit): ")

    if key == "?":
        print("The list: " + str(the_list))
    elif key == "q":
        break
    else:
        key = int(key)
        index = binary_search(the_list, key)
        if index == None:
            print(str(key) + " not found")
        else:
            print(str(key) + " found at index " + str(index))