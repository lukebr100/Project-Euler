# What is the largest prime factor of the number 600851475143?

import math
import time
import matplotlib.pyplot as plt 
def isPrime(n):
    L = round(math.sqrt(n))
    for i in range(2, L + 1):
        if n % i == 0:
            return 0
    return 1
def primeFactors(n, t):
    L = n
    for i in range(2, L + 1):
        if n % i == 0 and isPrime(i) == 1:
            t.append(i)
            return primeFactors(round(n / i), t)
    return n, t
def largestPrimeFactor1(n):
    A = primeFactors(n, [])[1][-1]
    return A

t1 = time.time()
print(largestPrimeFactor1(600851475143))
t2 = time.time()
deltaT1 = t2 - t1
print(deltaT1)

def largestPrimeFactor(n):
    factors = []
    for i in range(1, round(n / 2)):
        if n % i == 0:
            factors.append(i)
            print(i)
    for i in range(len(factors)):
        print(i)
        if isPrime(factors[-(i + 1)]) == 1:
            return factors[-(i + 1)]
    

def largestPrimeFactor(n, primeFactors):
    for i in range(1, round(n / 2)):
        if n % i == 0:
            if isPrime(i) == 0:
                return largestPrimeFactor(round(n / i), primeFactors)
            elif isPrime(i) == 1:
                primeFactors.append(i)
    return primeFactors[-1]               
t1 = time.time()
print(largestPrimeFactor(600851475143, []))
t2 = time.time()
deltaT2 = t2 - t1
print(deltaT2)

xaxis = [1, 2]
height = [deltaT1, deltaT2]
plt.xlabel('two different algorithms')
plt.ylabel('time')
plt.title(label = "elapsed time to find largest prime factor of 600851475143", loc= 'center')
plt.bar(xaxis, height, tick_label = ['divide by primes', 'brute for loop'], 
        width = 0.8, color = ['black', 'black']) 
plt.show()
