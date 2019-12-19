# dynamic programming algorithm for computing a maximum-weight independent set of a path graph
# prints out a list of values of maximum-weight IS for each vertex and then the IS itself (tracing back)


size = 1000
g = [0]*(size + 1)
with open('mwis.txt', 'r') as doc:
    h = 0
    for line in doc:
        g[h] = int(line)
        h += 1

a = [0]*(size + 1)
a[0] = 0
a[1] = g[1]
for i in range(2, size):
    a[i] = max(a[i-1], a[i-2] + g[i])

S = []
i = size
while i >= 1:
    if a[i-1] >= a[i-2] + g[i]:
        i -= 1
    else:
        S.append(i)
        i -= 2

print(a)
print(S)
