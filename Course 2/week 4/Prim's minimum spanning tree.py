# Prim's minimum spanning tree algorithm
# prints out the value of the minimum spanning tree, not the tree itself


size = 500
g = []
with open('edges.txt', 'r') as doc:
    for line in doc:
        g.append(list(map(int, line.split())))
del g[0]

exp = [0]*size
X = [1]
exp[0] = 1
T = 0
while len(X) != size:
    cheapest = 100000
    for i in g:
        if exp[i[0]-1] + exp[i[1]-1] == 1:
            if i[2] < cheapest:
                cheapest = i[2]
                if exp[i[0]-1] == 0:
                    v = i[0]
                elif exp[i[1]-1] == 0:
                    v = i[1]
    T += cheapest
    X.append(v)
    exp[v-1] = 1

print(T)
