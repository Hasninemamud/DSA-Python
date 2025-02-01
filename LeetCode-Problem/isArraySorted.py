def sortedArr(arr):
    n = len(arr)
    if n == 1:
        return "Sorted" 
    if arr[n-1] <= arr[n-2]:
        return "Not Sorted"
    return sortedArr(arr[:n-1])

arr = [11,12,13,14,15]

print(sortedArr(arr))