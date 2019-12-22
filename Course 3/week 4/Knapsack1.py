# Knapsack algorithm
# prints out the value of the optimal solution


a = []
with open('knapsack1.txt', 'r') as doc:
    for line in doc:
        a.append(list(map(int, line.split())))
kn_size = a[0][0] + 1
n = a[0][1] + 1
del a[0]

A = [[]]*n
A[0] = [0]*kn_size
for i in range(1, n):
    A[i] = [0]*kn_size
    for x in range(kn_size):
        if a[i-1][1] <= x:
            A[i][x] = max(A[i-1][x], A[i-1][x-a[i-1][1]]+a[i-1][0])
        else:
            A[i][x] = A[i-1][x]
print(A[-1][-1])
