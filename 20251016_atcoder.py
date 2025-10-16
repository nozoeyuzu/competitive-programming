#ABC427_A

# S = input().strip()
# i = len(S)//2
# result = S[:i] + S[i+1:]

# print(result)

#ABC426_A

# X, Y = input().split()
# if X == 'Lynx':
#     print('Yes')
# elif X == 'Serval' and (Y == 'Ocelot' or Y == 'Serval'):
#     print('Yes')
# elif X == 'Ocelot' and Y == 'Ocelot':
#     print('Yes')
# else:
#     print('No')

#ABC426_A_別解
X, Y = input().split()
order = {'Ocelot':1, 'Serval':2, 'Lynx':3}
if order[X] >= order[Y]:
    print('Yes')
else:
    print('No') 