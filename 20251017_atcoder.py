#ABC425_A

N = int(input())
result = 0

for i in range(N+1):
    if i % 2 == 0:
        result += i**3
    else:
        result -= i**3

print(result)