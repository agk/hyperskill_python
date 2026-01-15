n = float(input())
if n < 2:
    print("Analytic")
elif n >= 2 and n <= 3:
    print("Synthetic")
elif n > 3:
    print("Polysynthetic")