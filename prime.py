def isprime(n):   # Checks whether a number is prime or not
    return(factors(n) == [1, n])

def factors(n):   # Checks for the factors of a number
    factorlist = []
    for i in range(1, n+1):
        if n%i == 0:
            factorlist = factorlist + [i]
    return factorlist

def prime(n):   # returns the list of prime numbers
    primelist = []
    for i in range(1, n+1):
        if isprime(i):
            primelist = primelist + [i]
    return primelist

print('The primes upto 10 are {}'.format(prime(10)))
