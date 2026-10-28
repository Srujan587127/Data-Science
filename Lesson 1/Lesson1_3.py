import numpy as np

linear_array = np.arange(1, 25)

print("Original Array:")
print(linear_array)

print("Original Shape:", linear_array.shape)

print("\n" + "=" * 50)

shapes = [(1, 24), (2, 12), (3,8), (4,6), (6,4), (8,3), (12,2), (24,1)]

for shape in shapes:
    reshaped_array = linear_array.reshape(shape)

    print("\nReshaped to:", shape)
    print(reshaped_array)
    print("Shape:", reshaped_array.shape)
    print("-" * 50)
    