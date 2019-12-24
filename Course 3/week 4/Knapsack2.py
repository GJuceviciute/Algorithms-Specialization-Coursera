# Knapsack algorithm for a big instance
# prints out the value of the optimal solution


a = []
with open('knapsack_big.txt', 'r') as doc:
    for line in doc:
        a.append(list(map(int, line.split())))
kn_size = a[0][0] + 1
n = a[0][1] + 1
del a[0]

A = [[]]*2
A[0] = [0]*kn_size
for i in range(1, n):
    A[1] = [0]*kn_size
    for x in range(kn_size):
        if a[i-1][1] <= x:
            A[1][x] = max(A[0][x], A[0][x-a[i-1][1]]+a[i-1][0])
        else:
            A[1][x] = A[0][x]
    A[0] = A[1]
print(A[-1][-1])
