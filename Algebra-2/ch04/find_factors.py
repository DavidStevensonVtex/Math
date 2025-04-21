def find_factors(num):
    factors = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            factors.append(i)
            if num // i != i:
                factors.append(num // i)
    factors.sort()
    return factors


number = 48
factors_of_number = find_factors(number)
print(f"Factors of {number} are: {factors_of_number}")
# Expected Output: Factors of 36 are: [1, 2, 3, 4, 6, 9, 12, 18, 36]
