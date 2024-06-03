def fibo(n,dp):
    if(n<=1):
        return n
    if(dp[n]!=-1):
        return dp[n]
    dp[n]=fibo(n-1,dp)+fibo(n-2,dp)
    return dp[n]
n=5
dp=[-1 for i in range(n+1)]
print(fibo(n,dp))

n=4
prev2=0
prev1=1
for i in range(2,n):
    curi=prev2+prev1
    prev1=curi
    prev2=prev1
print(prev1)