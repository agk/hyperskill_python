string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
count = 0
for c in string:
    for ch in vowels:
        if c == ch:
            count += 1
print(count)