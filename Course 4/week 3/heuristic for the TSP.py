# Nearest neighbour heuristic for the Travelling Salesman Problem(TSP)
# Prints out the distance of this traveling salesman tour


import math

g = []
with open('tsp_big.txt', 'r') as doc:
    for line in doc:
        line = list(map(float, line.split()))
        del line[0]
        g.append(line)

n = len(g)
ans = 0
unexp = [_ for _ in range(2, n)]
k = 1


def nearest_neighbour():
    global ans, unexp, k
    if len(unexp) == 1:
        last = unexp[0]
        d = math.sqrt((g[k][0] - g[last][0])**2 + (g[k][1] - g[last][1])**2)
        ans += d
        ans += math.sqrt((g[last][0] - g[1][0])**2 + (g[last][1] - g[1][1])**2)
        print(ans)
    else:
        d = 1e8
        for j in unexp:
            if math.sqrt((g[k][0] - g[j][0])**2 + (g[k][1] - g[j][1])**2) < d:
                d = math.sqrt((g[k][0] - g[j][0])**2 + (g[k][1] - g[j][1])**2)
                t = j
        k = t
        unexp.remove(k)
        ans += d


for _ in range(1, n-1):
    nearest_neighbour()
    
