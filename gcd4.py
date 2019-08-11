def gcd(m, n):
    i = min(m, n)  # Assigning min(m, n) to i

    while i > 0:
        if m%i == 0 and n%i == 0:
            return i
        else:
            i -= 1

print('The GCD of 14 and 63 is {}'.format(gcd(14, 63)))