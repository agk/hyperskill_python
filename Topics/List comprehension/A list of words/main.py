# work with the preset variable `words`
# words = ['apple', 'pear', 'banana', 'Ananas']
words_a = [w for w in words if w.startswith(('a', 'A'))]
print(words_a)
