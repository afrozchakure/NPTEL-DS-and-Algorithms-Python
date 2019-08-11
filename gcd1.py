def gcd(m,n):
    fm = []  # List of factors of m
    for i in range(1, m):
        if m%i == 0:
            fm.append(i)

    fn = []  # List of factors of n
    for j in range(1, n):
        if n%j == 0:
            fn.append(j)
                      
    cf = []  # List of common factors of m and n
    for k in fm:
        if n%k == 0:
            cf.append(k)

    # Alternate way of calculating common factor
    # cf = []
    # for k in fm:
    #     if k in fn:
    #         cf.append(k)

    return cf[-1]

print('The GCD of 14 and 63 is {}'.format(gcd(14, 63)))
