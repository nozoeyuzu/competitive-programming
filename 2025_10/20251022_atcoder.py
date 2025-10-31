#ABC423_B
#逆順リストが欲しいときはスライスを使う
N = int(input())
L = list(map(int, input().split()))
#L_reverse = L.reverse()
L_reverse = L[::-1]
first = 0
last = 0

for i in range(N):
    if L[i] == 1:
        first = i
        break

for i in range(N):
    if L_reverse[i] == 1:
        last = N-i-1
        break

print(last-first) 

