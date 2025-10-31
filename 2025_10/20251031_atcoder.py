#ABC414
# N, L, R = map(int, input().split())
# XY = [tuple(map(int, input().split())) for _ in range(N)]
# X,Y = zip(*XY)
# count = 0

# for i in range(N):
#     if X[i] <= L and Y[i] >= R:
#         count += 1

# print(count)

# N = int(input())
# c_list = []
# l_list = []
# for _ in range(N):
#     c, l = input().split()
#     c_list.append(c)
#     l_list.append(int(l))

# S = []
# total_length = 0
# for i in range(N):
#     total_length += l_list[i]
#     if total_length > 100:
#         print('Too Long')
#         exit()
#     S.append(c_list[i]*l_list[i])

# print(''.join(S))