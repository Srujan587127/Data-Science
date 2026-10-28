import numpy as np

linear_array=np.array([1,2,3,4,5,6])

slice_array = linear_array[0:4]

print("Original Array:", linear_array)
print("Sliced Array:", slice_array)

import numpy as np

arr = np.array([1,2,3,4,5])

slice_arr = arr[0:3]

slice_arr[0] = 100

print("Orignal Array:", arr)
print("Sliced Arrray:", slice_arr)

import numpy as np

arr = np.array([[1,2,3], [4,5,6],[6,7,8]])

result = arr[0:2, 1:3]

print(result)

import numpy as np

arr = np.array(
    [[[1,2,3], [4,5,6], [7,8,9]], [[10,11,12], [13,14,15], [16,17,18]]]
)

print("Original 3D Array:")
print(arr)

result = arr[0, 0:2, 0:2]

print("\nSliced Array:")
print(result)