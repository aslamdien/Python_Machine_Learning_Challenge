import numpy as np

x = np.arange(20)
print("Set Of Numbers: ")
print(x)

my_mean = np.mean(x)
print("My Mean is: ", my_mean)

my_std = np.std(x)
print("My Standard Deviation is:", my_std)

my_variance = np.var(x)
print("My Variance is:" , my_variance)
