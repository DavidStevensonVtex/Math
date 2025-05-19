import numpy as np

mean = 90
std_dev = 17
sample_size = 100000  # Number of samples to generate

# Generate the normal distribution and round to integers
data = np.random.normal(mean, std_dev, sample_size)  # Number of samples to generate

std_dev = np.std(data)
mean = np.mean(data)

print(f"Array length:                    {len(data)}")
print(f"Mean:                            {mean}")
print(f"Standard deviation (population): {std_dev}")
print(f"Standard deviation (sample):     {np.std(data, ddof=1)}")
print()

count = 0
for i in data:
    if 93 <= i <= 101:
        count += 1

print(data)
print(
    f"Number of samples out of 500 samples between 93 and 101: {500*count/sample_size}"
)
