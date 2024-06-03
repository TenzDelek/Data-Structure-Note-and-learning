queuelist=[]
queuelist.insert(0,"tenzin")
queuelist.insert(0,"delek")
print(queuelist) #insertion is always done on first position (auto shift)
queuelist.pop() # here the logic is fifo liked
print(queuelist)

#not a good approach as dynamic is the problem here 
#read the readme file to know more