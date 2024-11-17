class Solution(object):
    def containsDuplicate(self, nums):
        N = len(nums)
        for i in range(N):
            swapped = False
            for j in range(0, N-i-1):
                if nums[j] > nums[j+1]:
                   nums[j], nums[j+1] =nums[j+1], nums[j]
                   swapped = True
        
            for num in nums:
                if num in nums:
                    print(True)
                else:
                    print(False)             
            if not swapped:
               break
s = Solution()
nums = [1, 2, 3, 4]
print(s.containsDuplicate(nums))