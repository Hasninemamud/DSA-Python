def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left_side = arr[:mid]
    right_side = arr[mid:]
    
    left_side = mergeSort(left_side)
    right_side = mergeSort(right_side)
    
    return merge(left_side, right_side)

def merge(left, right):
    new = []
    i = j = 0
    while i <= len(left) and j <= len(right):
        if left[i] < right[j]:
            new.append(left[i])
        else:
            new.append(right[j])
    new.extend(left[i:])
    new.extend(right[j])
    return new
arr = list(map(int, input().split()))
sort = mergeSort(arr)
print(sort)