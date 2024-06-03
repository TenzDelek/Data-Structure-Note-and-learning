arr = [53, 1, 36, 103, 53, 5]
arr.sort()
result = []
#this one i did for breaking the element to each subarray
for number in arr:
    subarray = []
    for digit in str(number):
        subarray.append(int(digit))
    result.append(subarray)

print(result)

l = 0
r = len(arr) - 1
maxsum = -1
#main logic here is if common digit is find between two min and max element then 
#the flag of commondigit turns true
while l < r:
    cursum = 0
    commondigits = False
    for digit in result[l]:
        if digit in result[r]:
            commondigits = True
            break

    if not commondigits:
        cursum = arr[l] + arr[r]
        maxsum = max(cursum, maxsum)

    l += 1

print(maxsum)
