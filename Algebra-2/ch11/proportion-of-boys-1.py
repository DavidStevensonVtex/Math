import numpy as np

mean = 0.54
std_dev = 0.05
sample_size = 50  # Number of samples to generate

# Generate the normal distribution and round to integers
data = np.round(
    np.random.normal(mean, std_dev, sample_size),
    decimals=2,  # Number of samples to generate
)


std_dev = np.std(data)
mean = np.mean(data)

print(f"Array length:                    {len(data)}")
print(f"Mean:                            {mean}")
print(f"Standard deviation (population): {std_dev}")
print(f"Standard deviation (sample):     {np.std(data, ddof=1)}")
print()

sorted_data = np.sort(data)
print(sorted_data)

with open("proportion-of-boys-1.txt", "w") as f:
    for d in sorted_data:
        f.write(f"{d:.2f}\n")
