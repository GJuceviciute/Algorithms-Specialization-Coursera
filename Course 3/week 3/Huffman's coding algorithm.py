# greedy Huffman's coding algorithm (using weights instead of frequencies of elements)
# printing lengths of the longest and shortest codewords in the resulting Huffman code


import heapq
size = 1000
t = [0]*(size + 1)
with open('huffman.txt', 'r') as doc:
    h = 0
    for line in doc:
        t[h] = int(line)
        h += 1
del t[0]
T = t.copy()
print(T)
heapq.heapify(T)
print(T)
shortest = 0
longest = 0
mini = min(t)
maxi = max(t)
while len(T) > 2:
    a = heapq.heappop(T)
    b = heapq.heappop(T)
    if a == mini or b == mini:
        longest += 1
        mini = a + b
    if a == maxi or b == maxi:
        shortest += 1
        maxi = a + b
    heapq.heappush(T, a + b)
if max(t) not in T:
    longest += 1
    shortest += 1
else:
    longest += 1

print(longest, shortest)
