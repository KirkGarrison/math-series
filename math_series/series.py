
# change x variable value to find the nth position of the fibonacci sequence

x = 6

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
 
print(fibonacci(x))

# change x variable above to find the nth positional value of the lucas sequence

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

print(lucas(x))

# change x variable above to find the nth positional value of the sum_series sequence (with default fibonacci args)

def sum_series(n, sequence_first=0, sequence_second=1):
    if n <= sequence_first or n <= sequence_second:
        return n
    else:
        return sum_series(n-1, sequence_first, sequence_second) + sum_series(n-2, sequence_first, sequence_second)

print(sum_series(x, sequence_first=0, sequence_second=1))

