# Actual Euclid GCD Algorithm

def gcd(m, n):
    if m < n:
        (m, n) = (n, m)  # Assume m >= n
    
    if m%n == 0:  # if remainder is 0 (m%n is the remainder)
        return n
    else:
        return gcd(n, m%n)  # m%n < n, always!!

def gcd_while(m, n):
    if m < n:
        (m, n) = (n, m)  # Assume m >= n

    while(m%n !=0):
        (m, n) = (n, m%n)  # m%n < n, always!!
    
    return(n)  # Finally returning n

print('The GCD of 14 and 63 is {}'.format(gcd(14, 63)))