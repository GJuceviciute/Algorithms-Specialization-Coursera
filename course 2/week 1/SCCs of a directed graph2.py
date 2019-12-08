# Counting SCCs of a directed graph iteratively
# prints out lengths of 5 biggest SCCs or 0s if there are less than 5 SCCs in the graph


size = 875714
g = [[] for _ in range(size)]
with open('SCC.txt', 'r') as fh:
    for line in fh:
        h = list(map(int, line.split()))
        g[h[0]-1].append(h[1])
rev = [[] for _ in range(size)]
with open('SCC.txt', 'r') as fh:
    for line in fh:
        k = list(map(int, line.split()))
        rev[k[1]-1].append(k[0])
t = 0
s = 1
exp1 = [0 for _ in range(size)]
exp2 = [0 for _ in range(size)]
tlist = [[] for _ in range(size)]
ti = [0 for _ in range(size)]
leader = [0 for _ in range(size)]
stack = []
tim = []


def SCCs(g):
     DFSloop1()
     TL(g, ti)
     DFSloop2()


def DFSloop1():
    global exp1, t, ti, stack, tim
    for v in range(size, 0, -1):
        if not exp1[v-1]:
            exp1[v-1] = 1
            stack.append(v)
            tim.append(v)
            while len(stack) > 0:
                vi = stack[-1]
                timlen = len(tim)
                del stack[-1]
                for j in rev[vi-1][::-1]:
                    if not exp1[j-1]:
                        exp1[j-1] = 1
                        stack.append(j)
                        tim.append(j)
                if len(tim) == timlen:
                    for p in range(len(tim)-1, -1, -1):
                        t += 1
                        ti[tim[p]-1] = t
                        if len(stack) > 0 and tim[p] == vi:
                            del tim[p]
                            break
                        del tim[p]


def DFSloop2():
    global s, exp2, leader
    for ve in range(size, 0, -1):
        if not exp2[ve-1]:
            exp2[ve-1] = 1
            s = ve
            leader[ve-1] = s
            stack.append(ve)
            while len(stack) > 0:
                ver = stack[-1]
                leader[ver-1] = s
                del stack[-1]
                for j in tlist[ver-1]:
                    if not exp2[j-1]:
                        exp2[j-1] = 1
                        stack.append(j)


def TL(g, ti):
    global tlist
    for n in range(size):
        for node in range(len(g[n])):
            tlist[ti[n]-1].append(ti[g[n][node]-1])


SCCs(g)

d = [0]*size
for m in leader:
    d[m-1] += 1
for _ in range(5):
    if max(d) > 0:
        print(max(d))
        d.remove(max(d))
    else:
        print(0)
