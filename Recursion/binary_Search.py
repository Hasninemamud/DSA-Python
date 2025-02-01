def binarySearch(arr, n):
    if n == 0 or n == 1:
        return True
    return arr[n-1] >= arr[n-2] and binarySearch(arr, n-1)
    
arr = [1,2,3,10,5,6,7]
n = len(arr)
b = binarySearch(arr, n)
print(b)