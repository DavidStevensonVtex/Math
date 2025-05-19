import numpy as np

mean = 40
std_dev = 15
sample_size = 100000  # Number of samples to generate

# Generate the normal distribution and round to integers
data = np.round(
    np.random.normal(mean, std_dev, sample_size)  # Number of samples to generate
).astype(int)

std_dev = np.std(data)
mean = np.mean(data)

print(f"Array length:                    {len(data)}")
print(f"Mean:                            {mean}")
print(f"Standard deviation (population): {std_dev}")
print(f"Standard deviation (sample):     {np.std(data, ddof=1)}")
print()

count = 0
for i in data:
    if i < 20:
        count += 1

print(
    "Percentage of exercise under 20 minutes with a mean of 40 and a standard distribution of 15:"
)
print(f"actual percentage: {100*count/sample_size}%")
