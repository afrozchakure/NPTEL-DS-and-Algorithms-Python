def gcd(m, n):
    cf = []  # Defining a list of common factors of m and n
    for i in range(1, min(m, n) + 1):
        if m%i == 0 and n%i == 0:
            mrcf = i  # Keeping track of 'most recent common factor'
    return mrcf

print('The GCD of 14 and 63 is {}'.format(gcd(14,63)))