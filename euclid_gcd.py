def gcd(m, n):
    # Assume m >= n
    if m < n:
        (m, n) = (n, m)  # Swapping values of m and n
    
    if (m%n) == 0:
        return n
    else:
        diff = m-n 
        # diff> n? Possible!
    return (gcd(max(n, diff), min(n, diff)))  # Making a recursive call

print('The GCD of 14 and 63 is {}'.format(gcd(14, 63)))