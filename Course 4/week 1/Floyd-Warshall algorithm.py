# Floyd - Warshall algorithm for all-pairs shortest-path problem
# prints out "NULL" when negative cycle is found, and "shortest shortest path"


n = 1001
g = [[[], []] for _ in range(n)]
with open('g1.txt', 'r') as doc:
    for line in doc:
        line = list(map(int, line.split()))
        if g[line[0]][0] and line[1] == g[line[0]][0][-1]:
            if line[2] < g[line[0]][1][-1]:
                g[line[0]][0][-1] = line[1]
                g[line[0]][1][-1] = line[2]
        else:
            g[line[0]][0].append(line[1])
            g[line[0]][1].append(line[2])


a = [[[0, 0] for _ in range(n)]for _ in range(n)]
for i in range(1, n):
    for j in range(1, n):
        if i == j:
            a[i][j][0] = 0
        if j in g[i][0]:
            ind = g[i][0].index(j)
            a[i][j][0] = g[i][1][ind]
        elif i != j and j not in g[i][0]:
            a[i][j][0] = 1e10

for k in range(1, n):
    for i in range(1, n):
        for j in range(1, n):
            a[i][j][1] = min(a[i][j][0], a[i][k][0] + a[k][j][0])
            a[i][j][0], a[i][j][1] = a[i][j][1], 0
    for h in range(n):
        if a[h][h][0] < 0:
            print('NULL')


print(min(min(a))[0])
