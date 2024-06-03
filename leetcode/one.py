import heapq

def min_operations_to_exceed_threshold(nums, k):
    operations = 0
    heapq.heapify(nums)
    print(f'after heapq: {nums}')
    while nums[0] < k:
        x = heapq.heappop(nums)
        y = heapq.heappop(nums)
        print(f'i was poped:{x} and {y}')
        new_element = min(x, y) * 2 + max(x, y)
        print(f'i am the new element pushed {new_element}')
        print(f'heap before push: {nums}')
        heapq.heappush(nums, new_element)
        operations += 1
        print(f'i am the array: {nums}')
    return operations

# Example usage:
nums = [ 2,1,4,3,5]
k = 10
result = min_operations_to_exceed_threshold(nums, k)
print(result)
