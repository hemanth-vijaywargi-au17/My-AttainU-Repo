"""
There is a sequence of numbers called the fibonacci numbers where each number
can be calculated as the sum of the last 2 numbers before it.
0,1,1,2,3,5,8,13,....
In the above sequence you can see that the fourth number 2 is the sum of the
second and third number 1 and 1. The fifth number 3 is the sum of 2 (fourth
number) and 1 (third number) and so on.
Read More Here on this: https://en.wikipedia.org/wiki/Fibonacci_number
Write a function fibonacci(n) which returns the nth fibonacci number. This
should be calculated using the while loop. The default value of n should be 10.
fibonacci(1)
# >>>0
fibonacci(2)
# >>>1
fibonacci(3)
# >>>1
fibonacci(4)
# >>>2
fibonacci(5)
# >>>3
Also find the maximum of:
fibonacci(12)+fibonacci(10) and fibonacci(11)+fibonacci(11).
"""


def fibonacci(n=10):
    if n == 1:
        next_value = 0
    elif n == 2:
        next_value = 1
    else:
        first_value = 0
        second_value = 1
        i = 3
        while i <= n:
            next_value = first_value + second_value
            first_value = second_value
            second_value = next_value
            i = i + 1
    return next_value


a = fibonacci(12) + fibonacci(10)
b = fibonacci(11) + fibonacci(11)
print(f"(a) 12!+10! = {a} \n(b) 11!+11! = {b}")
print("Maximum :", max(a, b))
