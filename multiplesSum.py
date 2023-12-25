# Find the sum of all multiples of 3 or 5 below 1000
def mutiplesSum(n, m, k):
    count = 0
    for i in range(k):
        if i % n == 0 or i % m == 0:
            count = count + i
    return count
            
print(mutiplesSum(3, 5, 1000))
