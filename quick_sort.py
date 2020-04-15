import random
array = list(range(1, 10))
random.shuffle(array)

""" array = [2, 8, 6, 0, 1, 7, 5, 4, 3, 9]
pivor = 2
smaller = 0, 1
larger = [8, 6, 7, 5, 4, 3, 9]

sort(smaller) + [2] + sort(larger)

quicksort([0, 1]) + [2] + quicksort([8, 6, 7, 5, 4, 3, 9])

quicksort([0, 1])

pivot = 0
smaller = []
larger = [1]

return quicksort([]) + [0] + quicksort([8, 6, 7, 5, 4, 3, 9])

[8, 6, 7, 5, 4, 3, 9]
pivot = 8
smaller = [6, 7, 5, 4, 3]
larger[9]

# quicksort[smaller] + [8] + quicksort([8, 6, 7, 5, 4, 3, 9])
return quicksort([6, 7, 5, 4, 3]) + [8] + [larger]

pivot = 6
# ... etc etc etc """


def quicksort(arr):
    # Base case: arr len 0 or 1 is sorted
    if len(arr) <= 1:
        return arr
    # Pick a pivot
    pivot = arr[0]
    print("Starting Array", array)
    print("Pivot", pivot)
    # Separate all vals smaller and larger than pivot
    smaller = []
    larger = []
    for i in range(1, len(arr)):
        # Sort smaller and larger
        if arr[i] <= pivot:
            smaller.append(arr[i])
            print("\nSmaller", smaller)
        else:
            larger.append(arr[i])
            print("Larger", larger)
    smaller = quicksort(smaller)
    larger = quicksort(larger)
    # Concatenate smaller + pivot + larger
    return smaller + [pivot] + larger


print(quicksort(array))
