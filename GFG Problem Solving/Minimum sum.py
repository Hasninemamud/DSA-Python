
class Solution:
    def minSum(self, arr):
    
    # Step 1: Sort the array
        arr.sort()
    
    # Step 2: Divide digits into two numbers
        num1, num2 = "", ""
        for i in range(len(arr)):
           if i % 2 == 0:
               num1 += str(arr[i])
           else:
               num2 += str(arr[i])
    
    # Step 3: Convert the two numbers to integers and calculate their sum
        result_sum = int(num1) + int(num2)
    
    # Step 4: Return the sum as a string
        return str(result_sum)