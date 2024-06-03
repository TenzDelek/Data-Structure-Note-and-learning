#fibo
#the time complexity will be O(2**n)->not exact
#exponentail as each fibo call 2 inner fibo
def fibo(n):
    if(n<=1):
        return n
    
    last= fibo(n-1)
    slast=fibo(n-2)
    return last+slast

print(fibo(4))