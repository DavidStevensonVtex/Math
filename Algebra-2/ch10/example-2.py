import numpy as np

mean = 55
std_dev = 15
sample_size = 10000  # Number of samples to generate

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
    if i >= 80:
        count += 1

print("Percentage of days with temperature 80 degrees or higher")
print(f"Expected percentage: 5% actual percentage: {100*count/sample_size}%")
