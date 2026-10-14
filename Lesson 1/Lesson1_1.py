import numpy as np

arr = np.array([5, 6, 7, 8, 9, 10])
print("1D Array:", arr)
print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)

arr2 = np.array([[1, 2, 3], [5, 6, 7]])
print("2D Array:", arr2)
print("Dimensions:", arr2.ndim)
print("Shape:", arr2.shape)

arr3 = np.array([
    [
        [1, 2],
        [3, 4],
        
    
    ],
    [
        [4, 5],
        [6, 7]

    ]
])
print("2D Array:", arr3)
print("Dimensions:", arr3.ndim)
print("Shape:", arr3.shape)

arr4 = np.zeros(10)
print(arr4)

arr5 = np.zeros((3,4))
print(arr5)

arr6 = np.ones(10)
print(arr6)

arr7 = np.ones((3,4))
print(arr7)

arr8 = np.arange(0, 20, 2)
print(arr8)

arr9 = np.arange(1, 10)
new_arr = arr.reshape(2, 2)
print(new_arr)