import numpy as np

mean = 50
std_dev = 3
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
    if 42 <= i <= 52:
        count += 1

print("Percentage of children with weights between 42 and 52 pounds:")
print(f"Expected percentage: 5% actual percentage: {100*count/sample_size}%")
