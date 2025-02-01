class Solution:
    def myPow(self, x: float, n: int) -> float: 
        binForm = n
        if n < 0:
            x = 1 / x  # Handle negative exponent by taking reciprocal
            binForm = -binForm  # Work with the positive exponent
        
        ans = 1
        while binForm > 0:
            if binForm % 2 == 1:  # Check if the current power is odd
                ans *= x  # Multiply the result by x
            x *= x  # Square the base
            binForm //= 2  # Use integer division to halve the power
        
        return ans
