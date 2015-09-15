# Euler problem number 12
# 
# Generates the smallest triangle number with more than 500 divisors
# Keywords: triangle numbers, divisors

import math

def triangle(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
    
    
    
def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n)+1)):
        if n % i is 0:
            yield i
            if i is not n/i:
                large_divisors.insert(0, n / i)
    for divisor in large_divisors:
        yield divisor

row = []
for number in range(1,100001):
    triNumber= triangle(number)
    divs = len(list(divisorGenerator(triNumber)))
    row.append([triNumber,divs])
    if divs > 500:
        print triNumber
        break
    
    
    
    
    
    
    
