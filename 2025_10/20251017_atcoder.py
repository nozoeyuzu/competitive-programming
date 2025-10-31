#ABC425_A

# N = int(input())
# result = 0

# for i in range(N+1):
#     if i % 2 == 0:
#         result += i**3
#     else:
#         result -= i**3

# print(result)

#ABC424_A

# a,b,c = map(int, input().split())
# if a!=b and b!=c and c!=a:
#     print('No')
# else:
#     print('Yes')

#ABC423_A
X, C = map(int, input().split())
max = (X * 1000) // (1000 + C)
max = (max // 1000) * 1000

print(max)