from math import *

def isPrime(number):
    if number == 1:
        return False
    for i in range (2, number):
        if number%i == 0:
            return False
    return True



def largestPrimeFactor(number):
    lp = number
    for i in range (round(sqrt(number)), 2, -1):
        if number%i == 0 and isPrime(i):
            lp = i
            return lp
    return lp

print(largestPrimeFactor(600851475143))
