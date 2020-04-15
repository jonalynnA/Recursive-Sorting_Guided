# TO-DO: Complete the selection_sort() function below
import random
array = list(range(1, 10))
random.shuffle(array)
print(f"Shuffle Sort{array}")
# [4, 3, 6, 8, 7, 9, 2, 5, 1]
'''
[4,             3, 6, 8, 7, 9, 2, 5, 1]
[3,             4, 6, 8, 7, 9, 2, 5, 1]
[3,4            6, 8, 7, 9, 2, 5, 1]
[3,4,6          8, 7, 9, 2, 5, 1]
^^^             ^^^
sorted side     unsorted side
'''


def selection_sort(arr):
    # loop through n-1 elements
    # n=1 because the one remaining will be the largest
    for i in range(0, len(arr) - 1):
        print(arr)
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # (hint, can do in 3 loc)

        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
    return arr


print(selection_sort(array))

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    # Make a flag to show if swaps have occured
    swaps_occured = True
    while swaps_occured:
        swaps_occured = False
    # For each element in the array...
    for i in range(len(arr) - 1):
        print(arr)
        # Chek it's neighbor to the right...
        if arr[i] > arr[i + 1]:
            # If neighbor is smaller, swap and make Flag true
            arr[i], arr[i+1] = arr[i+1], arr[i]
        # If you get to the end and swaps have occured, start again
    return arr


print("\nBubble Sort\033[34 m")
random.shuffle(array)
print(array)
print("")
print(bubble_sort(array))
