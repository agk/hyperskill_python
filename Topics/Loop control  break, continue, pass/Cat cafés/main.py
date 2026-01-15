cn = []
cc = []
while True:
    string = input()
    if string == 'MEOW':
        break
    else:
        cafe = string.split()
        cn.append(cafe[0])
        cc.append(int(cafe[1]))

index = cc.index(max(cc))
print(cn[index])
