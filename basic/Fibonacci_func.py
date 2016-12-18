def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


def Dump_Fibonacci(n, val):
    print "Fibonacci(%d) = %d\n" % (n, val)


n = 10
val = Fibonacci(n)
Dump_Fibonacci(n, val)
