import numpy as np

matrix = np.arange(1,50).reshape(7,7)

print(matrix)

import numpy as np

matrix = np.arange(1,50).reshape(7,7)

middle = matrix[2:5, 2:5]

print(middle)

import numpy as np

k = np.array([1,2,3,4,5,6,7,8])

even_numbers = k[k % 2 == 0]

print(even_numbers)

import numpy as np

arr = np.array([10, 25, 50 , 75, 100])

result = arr[arr > 50]

print(result)

import numpy as np

sample_array = np.array([1,2,3,4])

sample_array +=1

print(sample_array)