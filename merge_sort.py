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
