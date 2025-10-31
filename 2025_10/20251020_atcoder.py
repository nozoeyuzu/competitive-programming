#ABC427_B
# N = int(input())
# sum = 0
# total = 0
# for i in range(N+1):
#     sum += i
#     total += sum
# print(total)

# N = int(input())
# A = 1
# for _ in range(N-1):
#     A += sum(map(int, str(A)))
# print(A)

#ABC426_B
# S = input()
# for i in range(len(S)-1):
#     if S[i] != S[i+1]:
#         if i == 0:
#             if S[1] == S[2]:
#                 print(S[0])
#             else:
#                 print(S[1])
#             break
#         else:
#             if S[0] == S[i]:
#                 print(S[i+1])
#             else:
#                 print(S[i])
#             break

#ABC425_B
N = int(input())
A = list(map(int, input().split()))

used = [x for x in A if x!=-1]
used_ = set(used)
if len(used) == len(used_):
    if len(used) > 0:
        if max(used) <= N:
            print('Yes')
            lst = [i for i in range(1, N+1) if i not in used_]
            count = 0
            for i in range(N):
                if A[i] == -1:
                    A[i] = lst[count]
                    count += 1
            print(*A)
        else:
            print('No')
    else:
        print('Yes')
        A = [i for i in range(1, N+1)]
        print(*A)
else:
    print('No')
