# Papadimitriou's algorithm for 2SAT problem with some reductions beforehand
# prints out 'yes' if satisfiable and 'no' if not


import math
import random

h = []
with open('2sat1.txt', 'r') as doc:
    for line in doc:
        h += list(map(int, line.split()))

n = h[0]
del h[0]


def remove_always_satisfiable():  # removes all clauses that include 'x'/'-x', if there is only 'x' or only '-x' in g
    global h
    d = {h[i]: 0 for i in range(len(h))}
    h1 = []
    c = 0
    for i in range(0, len(h)-1, 2):
        if -h[i] not in d or -h[i+1] not in d:
            h[i] = 0
            h[i+1] = 0
            c = 1
        else:
            h1 += [h[i], h[i+1]]
    h = h1
    if c != 0:
        remove_always_satisfiable()


remove_always_satisfiable()

di = {h[i]: 0 for i in range(len(h)) if h[i] > 0}


def Papadimitrious_2SAT():
    if len(di) == 0:
        return 'yes'
    else:
        m = int(math.log2(len(di))) + 1
        for _ in range(m):
            dic = random_dictionary()
            for k in range(2*(len(dic))**2):
                count = 0
                for i in range(0, len(h), 2):
                    if h[i] > 0 and dic[h[i]] or h[i] < 0 and not dic[-h[i]]:
                        count += 1
                    elif h[i + 1] > 0 and dic[h[i + 1]] or h[i + 1] < 0 and not dic[-h[i + 1]]:
                        count += 1
                    else:
                        a = random.choice([i, i+1])
                        dic[abs(h[a])] = not dic[abs(h[a])]
                        break
                if count == len(h) // 2:
                    return 'yes'
    return 'no'


def random_dictionary():
    dic = {}
    for x in di:
        dic[x] = random.choice([True, False])
    return dic


print(Papadimitrious_2SAT())
