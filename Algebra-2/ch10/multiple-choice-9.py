import numpy as np

mean = 19
std_dev = 5
sample_size = 100000  # Number of samples to generate

# Generate the normal distribution and round to integers
data = np.round(
    np.random.normal(mean, std_dev, sample_size)  # Number of samples to generate
)

std_dev = np.std(data)
mean = np.mean(data)

print(f"Array length:                    {len(data)}")
print(f"Mean:                            {mean}")
print(f"Standard deviation (population): {std_dev}")
print(f"Standard deviation (sample):     {np.std(data, ddof=1)}")
print()

count = 0
for i in data:
    if 18.5 <= i <= 19.5:
        count += 1

print(
    f"Probability that it will snow between 18.5 and 19.5 inches in a year: {100*count/sample_size}%"
)
