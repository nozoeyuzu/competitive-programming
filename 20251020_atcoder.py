#ABC427_B
# N = int(input())
# sum = 0
# total = 0
# for i in range(N+1):
#     sum += i
#     total += sum
# print(total)

N = int(input())
A = 1
for _ in range(N-1):
    A += sum(map(int, str(A)))
print(A)
