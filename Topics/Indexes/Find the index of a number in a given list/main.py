def find_index(input_string):
    # Convert the input string into two components:
    # a list of numbers and a target number
    data = input_string.split('\n')
    numbers = list(map(int, data[0].split()))
    target = int(data[1])

    # Your task is to find the index of the first occurrence of the target in the numbers list
    # If the target is not in the list, return -1

    # Write your code here
    for index, item in enumerate(numbers):
        if (target == item):
            return index
    return -1

print(find_index(input() + "\n" + input()))
