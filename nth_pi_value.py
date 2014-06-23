# Nth Digit of PI
"""

	Author	:	ANOOP P T
	Date	:	23/06/2014
 
	Problem	:	Find PI Value to entered limit

	
	
	
"""

limit = int(input("Enter a number : "))
num = 245850922
resultstr = ""
for n in range(0,limit+1):
    val = int(num / 78256779)
    rem = num % 78256779    
    resultstr = resultstr + str(val)
    if(n==0):resultstr=str(val)+"."
    num = rem * 100000000
print(resultstr)
