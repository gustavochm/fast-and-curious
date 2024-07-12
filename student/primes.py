def write_primes(n, path):
    '''
    Write primes under n to a specified file using the Sieve of Eratosthenes,
    optimized to use less memory by only considering odd numbers.
    :param n: int, The number to write primes under.
    :param path: str, The path to the file to write the primes to.
    :return: None
    '''
    if n < 2:
        return

    # Half-sized sieve, only for odd numbers
    sieve = [True] * ((n // 2) + 1)
    with open(path, 'w') as file:
        file.write("2\n") if n >= 2 else None

        for i in range(3, n + 1, 2):
            if sieve[i // 2]:
                file.write(f"{i}\n")
                for j in range(i * i, n + 1, 2 * i):
                    sieve[j // 2] = False