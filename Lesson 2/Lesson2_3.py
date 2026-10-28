import numpy as np

def solve(x):
    return 2 * x+ 3

x= np.array([1,2,3,4,5])

y = solve(x)

print(y)
import numpy as np

arr = np.array([1,2,3,4,5])

print("Orignal Array:", arr)

print("Slice:", arr[1:4])

print("Even Numbers:", arr[arr % 2 == 0])

print("Multiply by 2:", arr * 2)

def square(x):
    return x**2

print("Squared Values:", square(arr))