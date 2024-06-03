# Python code to implement the approach

# Function to build Monotonic
# increasing stack
def increasingStack(arr, N):
	# Initialise stack
	stk=[]
	
	for i in range(N):
		# Either stack is empty or
		# all bigger nums are popped off
		while(len(stk) > 0 and stk[len(stk) - 1] > arr[i]):
			stk.pop()
		stk.append(arr[i])
		
	N2 = len(stk)
	ans = [0]*N2
	j = N2 - 1
	
	# Empty Stack
	while(len(stk) != 0):
		ans[j] = stk[len(stk) - 1]
		stk.pop()
		j = j - 1
	
	# Displaying the original array
	print("The Array: ",end="")
	for i in range(N):
		print(arr[i],end=" ")
	print()
	
	# Displaying Monotonic increasing stack
	print("The Stack: ",end="")
	for i in range(N2):
		print(ans[i],end=" ")
	print()
	
# Driver code
arr = [1, 4, 5, 3, 12, 10]
N = len(arr)

# Function Call
increasingStack(arr,N)

# This code is contributed by Pushpesh Raj.
