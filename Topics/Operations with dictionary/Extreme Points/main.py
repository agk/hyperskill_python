# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())
# test_dict = {"a": 43, "b": 1233, "c": 8}
new = sorted(test_dict, key=test_dict.get)
print("min: " + new[0] +"\nmax: " + new[-1])