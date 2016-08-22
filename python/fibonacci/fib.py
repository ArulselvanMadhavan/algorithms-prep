def fib(n):
    a,b = 0.0,1.0
    for x in range(n):
        a,b = a+b, a
    return a

if __name__ == '__main__':
    result = fib(12)
    print(result)
