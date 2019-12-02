# sorting a list and counting inversions in O(n log n) time


with open('IntegerArray.txt', 'r') as fh:
    a = [int(line) for line in fh]

inv = 0


def sortandcountinv(a):
    global inv
    b, c = splitarr(a)
    if len(b) <= 2:
        if len(b) == 2:
            if b[1] < b[0]:
                b[0], b[1] = b[1], b[0]
                inv += 1
        if len(c) == 2:
            if c[1] < c[0]:
                c[0], c[1] = c[1], c[0]
                inv += 1
        return mergesorted(b, c)
    return mergesorted(sortandcountinv(b), sortandcountinv(c))


def splitarr(a):
    n = len(a)
    b = a[:n//2]
    c = a[n//2:]
    return b, c


def mergesorted(b, c):
    global inv
    d = []
    i = 0
    j = 0
    for k in range(len(b) + len(c)):
        if i == len(b):
            d.append(c[j])
            j += 1
        elif j == len(c):
            d.append(b[i])
            i += 1
        elif b[i] < c[j]:
            d.append(b[i])
            i += 1
        elif c[j] < b[i]:
            d.append(c[j])
            inv += len(b) - i
            j += 1

    return d


sortandcountinv(a)
print(inv)
