import string
letters = string.ascii_lowercase
double_alphabet = dict.fromkeys(letters)
for x in letters:
    double_alphabet[x] = x + x
# print(double_alphabet)
