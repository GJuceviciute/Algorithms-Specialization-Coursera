# quick sorting a list while also counting the number of comparisons


with open('QuickSort.txt', 'r') as fh:
    a = [int(line) for line in fh]

count = 0


def quicksortcompcount(a):
    global count
    if len(a) <= 1:
        return a
    if len(a) == 2:
        if a[0] > a[1]:
            a[0], a[1] = a[1], a[0]
        count += 1
        return a
    b, p, c = partition(a)
    return quicksortcompcount(b) + [p] + quicksortcompcount(c)


def partition(a):
    global count
    a = pivotchoice(a)
    i = 0
    for j in range(1, len(a)):
        if a[j] < a[0]:
            a[j], a[i+1] = a[i+1], a[j]
            i += 1
    a[0], a[i] = a[i], a[0]
    count += len(a) - 1
    return a[:i], a[i], a[i+1:]


def pivotchoice(a):
    # if the pivot is the median of first, middle and last elements of the list:
    
    # if len(a) % 2 == 0:
    #     m = len(a)//2 - 1
    # else:
    #     m = len(a)//2
    # if a[-1] != min(a[0], a[-1], a[m]) and a[-1] != max(a[0], a[-1], a[m]):
    #     a[0], a[-1] = a[-1], a[0]
    # if a[m] != min(a[0], a[-1], a[m]) and a[m] != max(a[0], a[-1], a[m]):
    #     a[0], a[m] = a[m], a[0]
    
    # if the pivot is the last element:
    
    # a[0], a[-1] = a[-1], a[0]
    
    # if the pivot is the first element:
        
    return a


print(quicksortcompcount(a))
print(count)
