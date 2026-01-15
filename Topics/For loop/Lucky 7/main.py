n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
for n in numbers:
    if n % 7 == 0:
        print(n ** 2)