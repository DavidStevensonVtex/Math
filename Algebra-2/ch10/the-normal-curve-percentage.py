# Since 68% of the numbers are expected to fall within one standard deviation of the mean,
# then approximately .68 ⋅ 400 = 272 should be between 60 - 4 = 56 inches and 60 + 4 = 64 inches.

import numpy as np


data = []
with open("the-normal-curve.txt", "r") as f:
    line = None
    while True:
        line = f.readline()
        if not line:
            break
        data.append(int(line.strip()))

data_length = len(data)


std_dev = np.std(data)
mean = np.mean(data)

within_one_deviation_of_mean = 0.68 * 400
within_two_deviation_of_mean = 0.95 * 400

print(f"Array length:                    {len(data)}")
print(f"Mean:                            {mean}")
print(f"Standard deviation (population): {std_dev}")
print(f"Standard deviation (sample):     {np.std(data, ddof=1)}")
print()
print(f"Within one std dev (68%):        {int(within_one_deviation_of_mean)}")
print(f"Within two std dev (95%):        {int(within_two_deviation_of_mean)}")
print()

lower = mean - 1 * std_dev
upper = mean + 1 * std_dev
count = 0
for i in data:
    if lower <= i <= upper:
        count += 1
print(f"Number with 1 std dev: {count}")

lower = mean - 2 * std_dev
upper = mean + 2 * std_dev
count = 0
for i in data:
    if lower <= i <= upper:
        count += 1
print(f"Number with 2 std dev: {count}")
