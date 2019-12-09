# Dijkstra's shortest path algorithm
# prints shortest paths (min distances) from starting point to 10 chosen nodes


size = 200
g = []
with open('DijkstraData.txt', 'r') as fh:
    for line in fh:
        g.append(list(line.split()))
for i in range(size):
    g[i] = g[i][1:]
    for j in range(len(g[i])):
        g[i][j] = list(map(int, g[i][j].split(',')))

x = [1]
a = [0]*size
while len(x) < size:
    b = []
    d = []
    for i in x:
        for j in g[i-1]:
            if j[0] not in x:
                b.append(j[0])
                d.append(a[i-1] + j[1])
    ind = d.index(min(d))
    x.append(b[ind])
    a[b[ind]-1] = min(d)

print(a[7-1], a[37-1], a[59-1], a[82-1], a[99-1], a[115-1], a[133-1], a[165-1], a[188-1], a[197-1])
