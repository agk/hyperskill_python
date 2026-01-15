strings = input().split()

res = {}
for str in strings:
    s = str.lower()
    if s in res:
        res[s] += 1
    elif s not in res:
        res[s] = 1
for k, v in res.items():
    print(f"{k} {v}")