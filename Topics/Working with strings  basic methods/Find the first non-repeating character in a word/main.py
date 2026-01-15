# Function to find the first non-repeating character
def find_non_repeating_char(word):
    # Write your code here
    count = {}
    for c in word:
        if c not in count:
            count[c] = 0
        count[c] += 1
    # print(count)
    for c in word:
        if count[c] == 1:
            return c
    else:
        return -1

# Taking input from the user
word = input().strip()

# Calling the function and printing the result
print(find_non_repeating_char(word))