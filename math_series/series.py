
# change n variable value to find the nth position of the fibonacci sequence

n = 6
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
 
print(fibonacci(n))

# change n variable value to find the nth position of the lucas sequence
n = 6
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

print(lucas(n))

n = 6
def sum_series(n, zero, first):
    if zero == 0:
        return 0
    elif first == 1:
        return 1
    else:
        return sum_series(n-1) + sum_series(n-2)
print(sum_series(n))
