import numpy as np
s = "0.98 1. nan 0.67 nan nan"
s = str.replace(s, 'nan', '0')
arr = np.array([])
for num in str.split(s):
	arr = np.append(arr, float(num))

# arr = np.array([0.99 1. 0.67 0.87 0.66 0.55])
print(np.average(arr))
