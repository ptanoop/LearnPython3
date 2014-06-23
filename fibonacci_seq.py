# Fibonacci Sequence
"""

	Author	:	ANOOP P T
	Date	:	23/06/2014
 
	Problem	:	Enter a number and have the program generate the Fibonacci
	                sequence to that number or to the Nth number.
	
	
"""

try:
    nth = int(input("Enter limit : "))
    a = 1
    b = 0
    c = 0
    for n in range(0,nth):
        c = a + b
        print(c)
        a = b
        b = c
except ValueError:
    print("Invalid input")
    
