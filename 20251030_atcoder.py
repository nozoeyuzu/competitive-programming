#ABC416
# N, L, R = map(int, input().split())
# S = input().strip()

# for i in range(L-1,R):
#     if S[i] != 'o':
#         print('No')
#         exit()
# print('Yes')

# S = input().strip()
# T = list(S)
# for i in range(len(S)):
#     if T[i] == '.':
#         if i == 0 or T[i-1] == '#':
#             T[i] = 'o'
# print(''.join(T))

#ABC415
# N = int(input())
# A = list(map(int, input().split()))
# X = int(input())

# for i in range(len(A)):
#     if A[i] == X:
#         print('Yes')
#         exit()
# print('No')

# S = input().strip()
# baggage = []

# for i in range(len(S)):
#     if S[i] == '#':
#         baggage.append(i+1)
# for i in range(0,len(baggage),2):
#     print(f"{baggage[i]},{baggage[i+1]}")