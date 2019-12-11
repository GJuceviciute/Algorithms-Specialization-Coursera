# Maintaining heaps of n/2 smallest and n/2 biggest elements and counting sum of medians of the given elements so far (as they arrive one by one)
# prints out the sum of medians once all the elements in the text file are received


import heapq
Hlow = []
Hhigh = []
k = 0
s = 0

with open('Median.txt', 'r') as doc:
    for line in doc:
        i = int(line)
        k += 1
        if not Hlow:
            heapq.heappush(Hlow, -i)
        elif not Hhigh:
            if i > abs(Hlow[0]):
                heapq.heappush(Hhigh, i)
            else:
                heapq.heappush(Hlow, -i)
        else:
            if abs(Hlow[0]) < i < Hhigh[0] or i < abs(Hlow[0]):
                heapq.heappush(Hlow, -i)
            else:
                heapq.heappush(Hhigh, i)
        if len(Hlow) - len(Hhigh) == 2:
            a = heapq.heappop(Hlow)
            heapq.heappush(Hhigh, abs(a))
        if len(Hhigh) - len(Hlow) == 2:
            a = heapq.heappop(Hhigh)
            heapq.heappush(Hlow, -a)
        if k % 2 != 0 and len(Hhigh) > len(Hlow):
            s += Hhigh[0]
        else:
            s += abs(Hlow[0])

print(s)
