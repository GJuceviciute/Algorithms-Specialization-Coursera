# Solving the 2-SUM problem using a hash table
# prints out the number of target sums t in a given range that have at least one pair of numbers adding up to it


from tqdm import tqdm
h = {}
with open('2sum.txt', 'r') as doc:
    for line in doc:
        h[int(line)] = 1

c = 0
for t in tqdm(range(-10000, 10001)):
    for key in h:
        if t - key in h and t - key != key:
            c += 1
            break

print(c)
