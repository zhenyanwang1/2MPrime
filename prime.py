import time
t1=time.monotonic()
import sympy
count=len(list(sympy.sieve.primerange(1,2000000+1))) #Range it up!
print(count)
t2=time.monotonic()
print("Time:{n}s".format(n=t2-t1))
