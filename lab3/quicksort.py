# Author: Alexander Marcoux
# Date: 1 March 2023
# Purpose: quicksort/partition a list


def partition(the_list, p, r, compare_func):
    pivot = the_list[r]

    # counters
    i = p - 1
    j = p

    # should terminate when j = r
    while j < r:
        if compare_func(the_list[j], pivot):
            # increment i counter
            i += 1

            # swap the_list[i] and the_list[j]
            temp = the_list[i]
            the_list[i] = the_list[j]
            the_list[j] = temp

            # increment j
            j += 1
        else:  # if the_list[j] > pivot
            # increment j
            j += 1

    # now swap pivot with the_list[i + 1]
    swap_pivot = the_list[i + 1]
    the_list[i + 1] = pivot
    the_list[r] = swap_pivot

    # return index of pivot
    return i + 1


def quicksort(the_list, p, r, compare_func):
    # if len of list is less than 2
    if r <= p:
        return
    else:
        # returns index of pivot
        q = partition(the_list, p, r, compare_func)

        # calling quicksort above and below the found pivot
        quicksort(the_list, p, q - 1, compare_func)  # for sublist to the left
        quicksort(the_list, q + 1, r, compare_func)  # for sublist to the right


# calling quicksort, with p = the first index and r = the last index
def sort(the_list, compare_func):
    quicksort(the_list, 0, len(the_list) - 1, compare_func)
