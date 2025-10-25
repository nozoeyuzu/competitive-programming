#ABC419_B
Q = int(input())
query = [input().strip().split() for _ in range(Q)]
x =[]

for i in range(Q):
    if query[i][0] ==  '1':
        x.append(int(query[i][1]))
    else:
        x.sort()
        print(x[0])
        x.pop(0)