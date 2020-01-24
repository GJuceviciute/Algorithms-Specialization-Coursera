# clustering algorithm for computing a max-spacing k-clustering
# using leaders in order to have lookups of O(1), which could be done with union-find
# prints out the maximum spacing of 4-clustering


g = []
with open('clustering1.txt', 'r') as doc:
    for line in doc:
        g.append(list(map(int, line.split())))
size = g[0][0]
del g[0]
g.sort(key=lambda x: x[-1])

k = 4
clusters = [[]] * size
for i in range(size):
    clusters[i] = [i+1]
cl = size
leaders = [0] * size
for b in range(size):
    leaders[b] = b+1

maxspacing = 0
for j in g:
    if cl != k:
        if leaders[j[0]-1] != leaders[j[1]-1]:
            if len(clusters[leaders[j[1]-1]-1]) > len(clusters[leaders[j[0]-1]-1]):
                clusters[leaders[j[1]-1]-1] += clusters[leaders[j[0]-1]-1]
                oldlead = leaders[j[0]-1]
                for h in clusters[leaders[j[0]-1]-1]:
                    leaders[h - 1] = leaders[j[1]-1]
                clusters[oldlead-1] = []
            else:
                clusters[leaders[j[0] - 1]-1] += clusters[leaders[j[1] - 1]-1]
                oldlead = leaders[j[1]-1]
                for h in clusters[leaders[j[1]-1]-1]:
                    leaders[h - 1] = leaders[j[0]-1]
                clusters[oldlead-1] = []
            maxspacing = j[-1]
            cl -= 1
    else:
        if leaders[j[0] - 1] != leaders[j[1] - 1] and j[-1] != maxspacing:
            maxspacing = j[-1]
            break

print(maxspacing)
