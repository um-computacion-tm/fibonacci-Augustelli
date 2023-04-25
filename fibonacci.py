def fibonacci(n):

    fib_seq = [0, 1]
    while fib_seq[-1] < n:
        next_num = fib_seq[-1] + fib_seq[-2]
        if next_num > n:
            break
        fib_seq.append(next_num)
    return fib_seq