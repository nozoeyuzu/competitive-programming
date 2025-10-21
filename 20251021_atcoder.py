#ABC424_B
N,M,K = map(int, input().split())
solved = [set() for _ in range(N+1)]
done = [False] * (N + 1)
complete = []

for _ in range(K):
    a, b = map(int, input().split())
    solved[a].add(b)
    if not done[a] and len(solved[a]) == M:
        done[a] = True
        complete.append(a)

if complete:
    print(*complete)