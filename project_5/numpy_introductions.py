import numpy as np

x = np.array([3, 7, 1, 9, 4, 2, 6])

#basic statistics
print(f"Mean: {np.mean(x):.1f}")
print(f"Median: {np.median(x):.0f}")
print(f"Max: {np.max(x)}")
print(f"Min: {np.min(x)}")
print(f"Sorted: {np.sort(x)}")

#logic masks
print(f"Greater than 3: {x[x>3]}")
print(f"Even numbers: {x[x % 2 == 0]}")
print(f"Odd numbers: {x[x % 2 != 0]}")

#random
print(f"Random integer number: {np.random.randint(1, 11)}")
print(f"Random float number: {np.random.uniform(0,1):.2f}")