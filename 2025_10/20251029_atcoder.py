#ABC428
# S, A, B, X = map(int, input().split())
# T = X//(A+B)
# U = X % (A+B)
# if U >= A:
#     print(S*A*(T+1))
# else:
#     print(S*T*A+S*U)

N, K = map(int, input().split())
S = input()
max = 0
result = []

for i in range(N-K+1):
    char = S[i:i+K]
    count = 0
    for j in range(N-K+1):
        if char == S[j:j+K]:
            count += 1
    if count > max:
        result = [char]
        max = count
    elif count == max:
        if char not in result:
            result.append(char)
print(max)
print(' '.join(sorted(result)))