from math import *

def isPrime(number):
    if number == 1:
        return False
    for i in range (2, int(0.5*number)):
        if number%i == 0:
            return False
    return True



def largestPrimeFactor(number):
    if not isPrime(number):
        for i in range (int(0.5*number), 2, -1):
            if number%i == 0 and isPrime(i):
                return i
    else:
        return number


print(largestPrimeFactor(600851475143))
