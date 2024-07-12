def write_primes(n, path):
    '''
    Write primes under n to a specified file.
    :param n: int, The number to write primes under.
    :param path: str, The path to the file to write the primes to.
    :return: None
    '''
    # # Delete the contents of the file if it already exists
    # open(path, 'w').close()

    # # Loop over all the possible prime numbers
    # # for i in range(2, n + 1):
    # #     # Check if the number is prime
    # #     if is_prime(i):
    # #         #If it is prime, write it to the file
    # #         with open(path, 'a') as file:
    # #             file.write(str(i) + '\n')

    # #optimized
    # primes = []
    # # Loop over all the possible prime numbers
    # for i in range(2, n+1):
    #     #if it is prime add it to a list
    #     if is_prime(i):
    #         primes += [str(i) + '\n']

    # # Write the list of primes to the file
    # with open(path, 'w') as file:
    #     file.writelines(primes)

    sieve = [True] * (n+1)
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False

    primes = [str(i) + '\n' for i in range(2, n+1) if sieve[i]]

    with open(path, 'w') as file:
        file.writelines(primes)
            



# def is_prime(n):
#     '''
#     Check if a number is prime.
#     :param n: int, The number to check.
#     :return: bool, True if the number is prime, False otherwise.
#     '''

#     # # 0, 1, and negative numbers are not prime
#     # if n < 2:
#     #     return False
    
#     # # 2 is the only even prime number
#     # if n == 2:
#     #     return True
    
#     # # All other even numbers are not prime
#     # if n % 2 == 0:
#     #     return False

#     if n == 2:
#         return True
    
#     if n <2  or (n % 2 == 0):
#         return False
    

    
#     # Consider all odd numbers from 3 to the square root of n
#     for i in range(3, int(n ** 0.5) + 1, 2):
#         # If a factor is found, the number is not prime
#         if n % i == 0:
#             return False
#     # If no factors have been found, the number is prime
#     return True
