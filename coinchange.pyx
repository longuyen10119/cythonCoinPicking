from libc.math cimport sqrt
def findCombiR(amount, coins, index, numCoins,lr,hr):
    if amount < 0:
        return 0
    if numCoins > hr:
        return 0
    if amount == 0 and numCoins>=lr:
        return 1
    if amount>0 and numCoins==hr:
        return 0
    cdef int num = 0
    cdef int coin = 0
    for coin in range(index, len(coins)):
        if amount>=coins[coin]:
            num += findCombiR(amount-coins[coin], coins, coin,numCoins+1,lr,hr)
        else:
            break
    return num


def testPrime(n):
    if n == 1 or n == 2:
        return False
    cdef int maxdivisor = <int>sqrt(n)
    cdef int i = 0 
    for i in range(3, maxdivisor+1, 2):
        if n % i == 0:
            return False
    return True


def generatePrimeList(n):
    primeList = [1, 2]
    for i in range(3, n, 2):
        if testPrime(i):
            primeList.append(i)
    primeList.append(n)
    return primeList
