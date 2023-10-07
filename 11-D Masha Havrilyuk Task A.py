n = int(input())
k1 = n
A = []
while k1 > 0:
    k2 = k1 % 10
    k1 = k1 // 10
    A.insert(0, k2)
for i in range(0, len(A), 1):
    print(A[i], end=' ')
