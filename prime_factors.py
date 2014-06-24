# Prime Factorization 
"""

	Author	:	ANOOP P T
	Date	:	24/06/2014
 
	Problem	:	Have the user enter a number and
	                find all Prime Factors (if there are any) and
	                display them.
	
	
"""
import math

def getNextPrime(num):    
    loopFlag = True
    while loopFlag:
        num = num + 1
        k = int(math.sqrt(num))        
        foundPrime = True
        for i in range(2,k+1):
            if num%i==0:
                foundPrime = False
                loopFlag = True                
                break
        if foundPrime: loopFlag = False
    return num

number = int(input("Enter number to find prime factors : "))
k = number
primeFacts = []
primes = 2
while k > 1:
    if k % primes == 0:
        primeFacts.append(primes)        
        k = int(k / primes)        
    else:        
        primes = getNextPrime(primes)        
print("Prime Factors = ",format(set(primeFacts)))
