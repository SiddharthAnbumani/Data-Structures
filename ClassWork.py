# REVERSE A STRING
def reverseString(s):
    for i in range(len(s) - 1, -1,-1):
        print(s[i],end="")
    return

reverseString('apple')

# Palindrome checker 
def isPalindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[-(i+1)]:
            return False
    return True

# power of number
def findPower(num,power):
    return num ** power

# Facroial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

# Fibonacci series 
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# Sum of digits
def sum_of_digit(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digit(n // 10)