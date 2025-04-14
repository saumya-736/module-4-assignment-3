# 1.   Defines a function named factorial that takes a number as an argument and calculates 
# its factorial using a loop or recursion.

def factorial(number):
    n=1
    for i in range(number,0,-1):
        n= n*i
    return n
result = factorial(5)
print(result)
              

# USING RECURSION 
# def factorial(number):
#     if number < 2:
#         return 1
#     else :
#         return number*factorial(number-1)
# result = factorial(5)
# print(result)
        
