n = 5
arr = [1, 2, 3, 4, 5]
maxSum = float("-inf")
currentSum = 0

for i in arr:  # Start of subarray
    currentSum = max(i, currentSum+i)
    maxSum = max(currentSum, maxSum)
print(maxSum)
        
        