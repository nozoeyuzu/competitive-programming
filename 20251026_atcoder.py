#ABC418_B
# S = list(input())
# S_reverse = S[::-1]
# first = 0
# last = 0
# t_count = 0

# for i in range(len(S)):
#     if S[i] == 't':
#         t_count += 1

# for i in range(len(S)):
#     if S[i] == 't':
#         first = i
#         break

# for i in range(len(S)):
#     if S_reverse[i] == 't':
#         last = len(S)-i-1
#         break

# if abs(last-first) >= 3:
#     result = (t_count-2)/(last-first-2)
#     print(result)
# else:
#     print(0)

S = input().strip()
N = len(S)
ans = 0.0

for i in range(N):
    if S[i] != 't':
        continue
    for j in range(i+2, N):
        if S[j] != 't':
            continue
        t = S[i:j+1]
        x = t.count('t')
        tmp = (x - 2) / (len(t) - 2)
        if tmp > ans:
            ans = tmp
print(f"{ans:.17f}")