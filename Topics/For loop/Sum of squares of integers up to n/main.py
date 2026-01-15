# Required library import
#import math

def sum_of_squares(n):
    # Your code here
    sum = 0
    for i in range (0, n+1):
        #print(i)
        sum += pow(i,2)
    return sum

# You can call the function with an integer argument like this:
print(sum_of_squares(int(input())))