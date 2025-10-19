#ABC421_A
# N = int(input())
# S = [input() for _ in range(N)]
# X, Y = input().split()
# X = int(X)

# if S[X-1] == Y:
#     print('Yes')
# else:
#     print('No')

#ABC420_A
# X, Y = map(int, input().split())
# if X+Y > 12:
#     print(X+Y-12)
# else:
#     print(X+Y)

#ABC419_A
# S = input()
# if S == 'red':
#     print('SSS')
# elif S == 'blue':
#     print('FFF')
# elif S == ('green'):
#     print('MMM')
# else:
#     print('Unknown')

#ABC418_A
# N = int(input())
# S = input()

# if S[N-3:N] == 'tea':
#     print('Yes')
# else:
#     print('No')

#ABC417_A
N, A, B = map(int, input().split())
S = input()
print(S[A:(N-B)])