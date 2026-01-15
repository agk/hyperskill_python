import math

x = int(input())
res = 1 / (1 + math.exp(-x))
# print('{0:.2f}'.format(res))
print(round(res, 2))
