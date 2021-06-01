import numpy as np
import matplotlib.pyplot as plt

nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
bins = np.array([0, 1, 2, 3])

plt.hist(nums, bins=bins, color = "green")
plt.xlabel("Nums", fontsize = "15")
plt.ylabel("Bins", fontsize = "15")
plt.title("Histogram of Nums against Bins.", fontsize = "20")
plt.show()
