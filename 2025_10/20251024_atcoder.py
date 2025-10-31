#ABC420_B
N, M = map(int, input().split())
S = [input().strip() for _ in range(N)]

total_score = [0 for _ in range(N)]

for j in range(M):
    x=0
    y=0
    x_list = []
    y_list = []
    for i in range(N):
        if S[i][j] == '0':
            x += 1
            x_list.append(i)
        else:
            y += 1
            y_list.append(i)
    if x==0 or y==0:
        for i in range(N):
            total_score[i] += 1
    elif x < y:
        for i in range(len(x_list)):
            total_score[x_list[i]] += 1
    else:
        for i in range(len(y_list)):
            total_score[y_list[i]] += 1

mx = max(total_score)
ans = [i+1 for i,s in enumerate(total_score) if s == mx]
print(*ans)