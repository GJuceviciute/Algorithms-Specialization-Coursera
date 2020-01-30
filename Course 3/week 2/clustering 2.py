# Clustering algorithm for computing clusters with spacing between them of at least 3
# distances defined as hamming distances between the given elements
# prints out the maximum amount of clusters with distance between any 2 elements in separate clusters being at least 3


size = 200000
bits = 24
g = [0] * (size + 1)
h = 0
with open('clustering_big.txt', 'r') as doc:
    for line in doc:
        g[h] = line.rstrip('\n').replace(' ', '')
        h += 1
del g[0]
g = [int(i, 2) for i in g]

variations = [[i] for i in g]
for i in range(size):
    for j in range(bits):
        variations[i].append(g[i] ^ 1 << j)
        for k in range(j+1, bits):
            variations[i].append((g[i] ^ 1 << j) ^ 1 << k)

d = {}
for i in range(size):
    if g[i] in d:
        d[g[i]] += [i]
    else:
        d[g[i]] = [i]

clusters = [-1 for _ in range(size)]
cluster_elements = {}

for i in range(size):
    for var in variations[i]:
        if var in d:
            if clusters[i] == -1:
                clusters[i] = i
                cluster_elements[i] = [i]
            for j in d[var]:
                if clusters[j] == -1:
                    clusters[j] = clusters[i]
                    cluster_elements[clusters[i]] += [j]
                elif clusters[i] != clusters[j]:
                    # print(i, var, j)
                    past_cluster = clusters[j]
                    cluster_elements[clusters[i]] += cluster_elements[past_cluster]
                    for e in cluster_elements[past_cluster]:
                        clusters[e] = clusters[i]
                    cluster_elements[past_cluster] = []


unique_clusters = set(clusters)
print(len(unique_clusters))
