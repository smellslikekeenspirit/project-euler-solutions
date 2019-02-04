def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)

print(fib(8))

def findSum():
    sum = 0
    i = 1
    while(True):
        s = fib(i)
        if s > 4000000:
            break
        elif s%2 == 0:
            sum+=s
        i += 1
    print(sum)

findSum()

