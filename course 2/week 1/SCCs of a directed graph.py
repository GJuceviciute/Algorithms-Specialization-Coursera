# Counting Strongly Connected Components (SCCs) of a directed graph recursively
# prints lengths of 5 biggest SCCs or 0s if there are less than 5


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

print(g[0])

def SCCs(g):
     DFSloop1()
     TL(g, ti)
     DFSloop2()


def DFSloop1():
    global rev, t, exp1
    for v in range(size, 0, -1):
        if not exp1[v-1]:
            DFS1(v)


def DFS1(v):
    global rev, t, exp1, ti
    exp1[v-1] = 1
    for j in rev[v-1]:
        if not exp1[j-1]:
            DFS1(j)
    t += 1
    ti[v-1] = t


def DFSloop2():
    global s, exp2
    for ve in range(size, 0, -1):
        if not exp2[ve-1]:
            s = ve
            DFS2(ve)


def DFS2(ve):
    global tlist, s, exp2, leader
    exp2[ve-1] = 1
    leader[ve-1] = s
    for j in tlist[ve-1]:
        if not exp2[j-1]:
            DFS2(j)


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
