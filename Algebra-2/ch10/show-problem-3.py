import numpy as np

mean = 66
std_dev = 8
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
    if i > 82:
        count += 1

# print(data)
print("Percentage of adult heights over 82 inches:")
print(f"actual percentage: {100*count/sample_size}%")
