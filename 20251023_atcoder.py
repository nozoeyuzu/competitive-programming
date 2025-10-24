#ABC422_B
# H, W = map(int, input().split())
# S = [input() for _ in range(H)]

# for i in range(H):
#     for j in range(W):
#         if S[i][j] == '#':
#             count = 0
#             for di, dj in [(-1, 0),(1, 0),(0, -1),(0, 1)]:
#                 k = i + di
#                 l = j + dj
#                 if 0<= k < H and 0 <= l < W and S[k][l] == '#':
#                     count += 1
#             if count not in [2, 4]:
#                 print('No')
#                 exit()
# print('Yes')

#ABC421_B 
# X, Y = map(int, input().split())
# a = [X,Y]
# for i in range(2,10):
#     b = a[i-1]+a[i-2]
#     b = str(b)
#     b = b[::-1]
#     a.append(int(b))
# print(a[9])