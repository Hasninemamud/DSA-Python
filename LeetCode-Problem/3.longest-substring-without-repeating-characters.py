class Solution:
    def lengthOfLongestSubstring(self, s):
        arr = []
        
        for i in range(len(s)):
            if s[i] not in arr:
                arr.append(s[i]) 
        print(arr)
        return len(arr)
        
S = Solution()
s = "pwwkew"
print(S.lengthOfLongestSubstring(s))

