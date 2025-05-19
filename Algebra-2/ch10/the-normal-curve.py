import numpy as np

mean = 60
std_dev = 4
size = 400  # Number of samples to generate

# Generate the normal distribution and round to integers
normal_dist_integers = np.round(np.random.normal(mean, std_dev, size)).astype(int)

sorted_arr = np.sort(normal_dist_integers)
with open("the-normal-curve.csv", "w") as f:
    for i in sorted_arr:
        f.write(str(i) + ", ")

with open("the-normal-curve.txt", "w") as f:
    for i in sorted_arr:
        f.write(str(i) + "\n")
