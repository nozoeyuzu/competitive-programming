#ABC417_B
# N, M = map(int, input().split())
# A = input().split()
# B = input().split()
# A_ = []

# for i in range(N):
#     for j in range(M):
#         if A[i] == B[j]:
#             A_.append(i)
#             continue
# result = [A[i] for i in range(N) if i not in A_]

# print(*result)

N, M = map(int, input().split())
A = input().split()
B = input().split()

for X in B:
    new = []
    flag = True
    for Y in A:
        if X == Y and flag:
            flag = False
        else:
            new.append(Y)
    A = new
print(*A)