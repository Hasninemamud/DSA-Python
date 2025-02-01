class Solution:
    def isPlalindrome(self, x):
        xStr = str(x)
        if x < 0:
            return 'flase'
        elif x == int(xStr[::-1]):
            return 'true'
        else:
            return 'flase'

s = Solution()
x = int(input())
print(s.isPlalindrome(x))