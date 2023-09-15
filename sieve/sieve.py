def primes(limit):
    primes=[num for num in range(2,limit+1)]
    [primes.remove(dividend) for divisor in primes for dividend in primes 
     if dividend!=divisor and dividend%divisor==0]                


    return primes
