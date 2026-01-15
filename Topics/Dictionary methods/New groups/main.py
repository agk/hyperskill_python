# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
dict_group = dict.fromkeys(groups)
# print(dict_group)
n = int(input())
for x in range(0, n):
    m = int(input())
    dict_group[groups[x]] = m

print(dict_group)