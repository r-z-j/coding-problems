'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
'''

def findFactors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    d = 3
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= 2
        d += 2
    if n > 1:
        factors.append(n)
    return factors

num = 600851475143
print(findFactors(num))
""" TODO: go through list of factors to find largest prime """ 
