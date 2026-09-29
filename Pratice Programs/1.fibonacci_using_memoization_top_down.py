# 1. Fibonacci Using Memoization										
										
# Develop a Python program to generate the Fibonacci sequence using Memoization (Top-Down Dynamic Programming).										
										
# Requirements										
# 	Accept an integer N.									
# 	Generate the first N Fibonacci numbers.									
# 	Store previously computed values.	


def fibonacci(n, memo):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

n = int(input("Enter a number: "))

memo = {}

# print("first" ,n , "fibonacci No's:")

for i in range(n):
    print(fibonacci(i, memo), end= " ")
