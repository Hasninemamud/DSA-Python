def insertion_sort(arr):
    N = len(arr)
    for i in range(1, N):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
arr = [20, 10, 40,25, 35]
print(insertion_sort(arr))