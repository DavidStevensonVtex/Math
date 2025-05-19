import numpy as np

mean = 9
std_dev = 2
sample_size = 1000  # Number of samples to generate

# Generate the normal distribution and round to integers
data = np.random.normal(mean, std_dev, sample_size)  # Number of samples to generate


data = np.sort(data)

std_dev = np.std(data)
mean = np.mean(data)

print(f"Array length:                    {len(data)}")
print(f"Mean:                            {mean}")
print(f"Standard deviation (population): {std_dev}")
print(f"Standard deviation (sample):     {np.std(data, ddof=1)}")
print()

# print(data)
# Top 5%: 5 * 1000/100 = 50 (index)
print(f"Running time: {data[49]} minutes")
