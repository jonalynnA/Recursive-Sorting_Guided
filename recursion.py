import random
'''             1. Must have a base case.
                2. Must change state toward the base case.
                3. Must call itself, recursively.
                Don't forget to either return your recursive call 
                OR 
                store the return of it in a variable that you can work with later on in the function
'''


def shuff(n=10):
    arr = list(range(n))
    random.shuffle(arr)
    return arr


def factorial(n):
    print(n)
    total = 1
    for i in range(n, 0, -1):
        total *= i
    return total


print("\nFactorial")
print(factorial(24))

# n! = n * (n-1)!


def factorial_r(n):
    print(n)
    if n <= 1:
        return 1
    return n * factorial_r(n-1)


print("\nFactorial Recursive")
print(factorial_r(5))
