# heap data structure is mainly used to represent
#priority queue

#python has heapq modules
import heapq

arr=[23,2,3,21]

heapq.heapify(arr)

print(f"the created heap is:{list(arr)} ")
# this brings the smallest element to the first
#swap the smallest with the first element

heapq.heappush(arr,12)
print('the modified heap after push:')
print(list(arr)) # here the 12 will swap with the first encounter which doesnt give true like 21>12 so it swap

print(heapq.heappop(arr)) #2
print(heapq.heappop(arr)) #3
print(heapq.heappop(arr)) #12
print(arr) #21 and 23