# Count primes using the Sieve of Eratosthenes
def count_primes(n):
    sorter_primes = [True] * n  # Create a list to represent the sieve
    sorter_primes[0] = sorter_primes[1] = False  # 0 and 1 are not primes
    for i in range(2, int(n**0.5) + 1):
        if sorter_primes[i]:
            for j in range(i*i, n, i):
                sorter_primes[j] = False
    return sum(sorter_primes)

# List of numbers to check
values = [10, 100, 1000, 10000, 100000, 1000000]
prime_counts = []

# Counting primes for each value in the list
for v in values:
    prime_counts.append(count_primes(v))

# Display the results
print("Number of primes less than:")
for v, count in zip(values, prime_counts):
    print(f"{v}: {count} primes")

# Predict the number of primes less than 10 million
prediction_value = 10000000
primes_less_than_10_million = count_primes(prediction_value)
print(f"Number of primes less than 10 million: {primes_less_than_10_million}")
