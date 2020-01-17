# Dynamic programming algorithm for Traveling Salesman Problem (TSP)
# prints out the minimum cost of a traveling salesman tour rounded down to the nearest integer


import math

g = []
with open('tsp.txt', 'r') as doc:
    for line in doc:
        g.append(list(map(float, line.split())))
n = int(g[0][0])
del g[0]
d = [[0.0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        d[i][j] = math.sqrt((g[i][0] - g[j][0])**2 + (g[i][1] - g[j][1])**2)

a = [[1e6 for _ in range(2**(n-1))] for _ in range(n-1)]
print(len(a))
print()
for i in range(n-1):
    a[i][1 << i] = d[0][i+1]

pos_bits = [0]*(2**(n-1))  # number of positive bits in binary numbers from 0 to 2**24
for i in range(2**(n-1)):
    pos_bits[i] = bin(i).count('1')

for m in range(3, n+1):
    for s in range(2**(n-1)):
        if pos_bits[s] == m-1:
            for j in range(2, n+1):
                if bin(s)[-j+1] == 'b':
                    break
                elif bin(s)[-j+1] == '1':
                    for k in range(2, n+1):
                        if bin(s)[-k+1] == 'b':
                            break
                        elif bin(s)[-k+1] == '1' and k != j:
                            a[j-2][s] = min(a[j-2][s], a[k-2][s-(1 << (j-2))] + d[k-1][j-1])

f = []
for j in range(2, n+1):
    f.append(a[j-2][2**(n-1)-1] + d[j-1][0])

print(int(min(f)))
