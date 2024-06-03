import heapq
def heap_sort(arr):
    heapq.heapify(arr)
    print(arr)
    sorted_result = []
    while arr:
        min_element = heapq.heappop(arr)
        print(arr)
        sorted_result.append(min_element)

    return sorted_result

unsorted_list = [4, 10, 3, 5, 1]
sorted_list = heap_sort(unsorted_list)
print("Sorted List:", sorted_list)
