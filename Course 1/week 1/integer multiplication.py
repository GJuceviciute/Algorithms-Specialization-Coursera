def mult(x,y):
    if len(str(x)) == 1 and len(str(y)) == 1:
        return x * y
    n = max(len(str(x)), len(str(y)))
    n1 = n // 2

    a = x//10**n1
    b = x % 10**n1
    c = y//10**n1
    d = y % 10**n1

    e = mult(a, c)
    f = mult(b, d)
    g = mult(a + b, c + d)
    h = g - f - e
    ans = 10 ** (n1*2) * e + 10 ** n1 * h + f
    return ans

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
print(mult(x, y))
