import numpy as np

mean = 15.3
std_dev = 9.9
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
    if i > 30:
        count += 1

print(f"Percentage of players with over 30 home runs: {100*count/sample_size}%")
