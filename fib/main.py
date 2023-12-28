def fib(n):
    i = 0
    fib_array = []
    if n < 2:
        return n
    elif n > 0:
        while i <= n:
            fib_array.append(i) if len(fib_array) < 2 else fib_array.append(sum(fib_array[-2:]))
            i += 1
    return fib_array[n]

if __name__ == '__main__':
    print(fib(5))
