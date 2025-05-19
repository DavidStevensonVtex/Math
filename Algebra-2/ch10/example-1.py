import numpy as np

mean = 80
std_dev = 15
sample_size = 500  # Number of samples to generate

# Generate the normal distribution and round to integers
data = np.round(
    np.random.normal(mean, std_dev, sample_size)  # Number of samples to generate
).astype(int)

std_dev = np.std(data)
mean = np.mean(data)

within_one_deviation_of_mean = 0.68 * sample_size
within_two_deviation_of_mean = 0.95 * sample_size

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

# Calculate number of scores between 74 and 89, which should be approximately 38%.

count = 0
for i in data:
    if 74 <= i <= 89:
        count += 1

print(f"Expected # of scores(74-89): {sample_size*.38}, actual: {count}")
print(f"Expected percentage: 38% actual percentage: {100*count/sample_size}%")
