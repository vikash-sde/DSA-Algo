

# <----- Recursion working in stack memory ----->

# def firstMethod():
#     secondMethod()
#     print("first call")

# def secondMethod():
#     thirdMethod()
#     print("Second call")

# def thirdMethod():
#     print("Third call")

# firstMethod()


# def recursiveMethod(n):
#     if n<1:
#         print("n is less than 1")
#     else:
#         recursiveMethod(n-1)
#         print(n)

# recursiveMethod(4)


# <----- Recursion vs iteration ----->


# <----- How to write recursion in 3 steps ----->

## Factorial###

# n! = n*(n-1)!
# 1! = 1, 0! = 1
# for negative, decimal number


# def factorial(n):
#     assert n>=0 and int(n) == n,' number must be positive integer'
#     if n in [0,1]:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(10))

## Fibonacci###
# 0,1,1,2,3,5,8,13..
# 5 = 3 + 2
# fn = fn-1 + fn-2

def finbonacci(n):
    assert n>=0 and int(n)== n,'Fibonacci number must be positive integer'
    if n in [0,1]:
        return n
    else:
        return finbonacci(n-1) + finbonacci(n-2)


print(finbonacci(6))

