#ABC422_A
# i,j = map(int, input().split('-'))
# if i < 8:
#     if j < 8:
#         print(i,'-',j+1)
#     else:
#         print(i+1,'-',1)

i, j = map(int, input().split('-'))
if j < 8:
    print(f"{i}-{j+1}")
else:
    print(f"{i+1}-1")