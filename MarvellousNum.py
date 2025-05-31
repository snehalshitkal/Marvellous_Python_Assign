def CheckPrime(num):
    if num < 0:
        return false

    for i in range(2,(num/2)+1):
        if num%i ==0:
            return false
        return true
    