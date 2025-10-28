#ABC429
# N, M = map(int, input().split())

# for i in range(N):
#     if i < M:
#         print('OK')
#     else:
#         print('Too Many Requests')

N, M = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if sum(A)-A[i] == M:
        print('Yes')
        exit()
print('No')
#↑計算量が大きい
