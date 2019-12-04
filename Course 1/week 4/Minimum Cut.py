#Karger's Minimum Cut algorithm with randomised edge contractions


import random
# import copy
a1 = []
with open('kargerMinCut.txt', 'r') as fh:
    for line in fh:
        a1.append(list(map(int, line.split())))


def MinCut(a):
    while len(a) > 2:
        a = edgecontractions(a)
    return len(a[0]) - 1


def edgecontractions(a):
    x, y = randomisation(a)
    ind = a.index(x)
    inde = 0
    for g in a:
        if g[0] == y:
            inde = a.index(g)
    while y in x:
        x.remove(y)
    for i in a[inde][1:]:
        if i != x[0]:
            x.append(i)
    a[ind] = x
    del a[inde]
    for j in range(len(a)):
        while y in a[j]:
            a[j].remove(y)
            a[j].append(x[0])
    return a


def randomisation(a):
    x = random.choice(a)
    y = random.choice(x[1:])
    return x, y


# m = 1e7
# for s in range(10000):
#     a2 = copy.deepcopy(a1)
#     zz = MinCut(a2)
#     if zz < m:
#         m = zz
#         print(m, a2)
