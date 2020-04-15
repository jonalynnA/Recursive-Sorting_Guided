import random
array = list(range(1, 10))
random.shuffle(array)

# Marge Sort


array_start = [2, 0, 1, 3, 6, 9, 8, 5, 7, 4]
# Split arrays in half
arr1 = [2, 0, 1, 3, 6]
arr2 = [9, 8, 5, 7, 4]

# Sort each half
arr1 = [0, 1, 2, 3, 6]
arr2 = [4, 5, 7, 8, 9]

# Merge them back together
merged = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge(arrA, arrB):
    print(f"    MERGING:{arrA} - {arrB}")
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements  # Allocating memory
    # Initialize pointers to the front of A and b arrays
    a = 0
    b = 0
    # Compare the first elements of A and B
    # Copy the smallest to merged_arr
    for i in range(elements):
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    print(f"SORTING: {arr}")
    # Base case: If the array is empty or length 1, return
    if len(arr) <= 1:
        return arr
# Split arrays in half
    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]
# Sort each half
    left = merge_sort(left)
    right = merge_sort(right)
# Merge them back together
    return merge(left, right)


arr = [2, 9, 7, 0, 8, 3, 1, 4, 6, 5]
print(merge_sort(arr))
