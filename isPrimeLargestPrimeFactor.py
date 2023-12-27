def isPrime(n):
    L = round(n / 2)
    for i in range(2, L + 1):
        if n % i == 0:
            return 0
    return 1
print(isPrime(5))
def largestPrimeFactor(n, primeFactors):
    for i in range(1, round(n / 2)):
        if n % i == 0:
            if isPrime(i) == 0:
                return largestPrimeFactor(round(n / i), primeFactors)
            elif isPrime(i) == 1:
                primeFactors.append(i)
    return primeFactors[-1]               
print(largestPrimeFactor(600851475143, []))
