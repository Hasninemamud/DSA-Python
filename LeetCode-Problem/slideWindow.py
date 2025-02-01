# k= int(input())
# nums = [2, 1, 5, 1, 3, 2]

# windowSum = sum(nums[:3])
# maxSum = windowSum

# for i in range(k, len(nums)):
#     windowSum += nums[i] - nums[i-k]
#     maxSum = max(windowSum, maxSum)
# print(maxSum)

k= int(input())
nums = [1,-1,-3,-2,3]
window = min(nums[:k])
minValue = [window]

for i in range(k, len(nums)):
    window = nums[i] - nums[i-k]
    minValue.append(window)
print(minValue)