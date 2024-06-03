from collections import deque

s="tenzin"
ans=deque(s)
print(ans)
# the reason we love to use deque over a normal list is that adding to starting is easy
ans.appendleft(3)
print(ans)

ans.append(44)
print(ans)

#also the poping is easy from the start and last
ans.popleft()

ans.pop()
print(ans)

#clearing all
ans.clear()
print(ans)

# to extend multiple thing - only on iterable object like string list not int
ans.extend("tenzin")
print(ans)
ans.extend("delek")
print(ans)

#extending to left
ans.extendleft([1,0,1,0])
print(ans)

#rotating -> -ve mean leftshift and +ve is rightshift

ans.rotate(-1) #left shift
print(ans)

ans.rotate(2) # right shift
print(ans)

#------------------------------
#Maxlen
res=deque("tenzin",maxlen=6)
print(res)
res.extend([1,1,1]) # as the maxlen is 6 and you are trying to add more it delete from the starting like a fifo
print(res)