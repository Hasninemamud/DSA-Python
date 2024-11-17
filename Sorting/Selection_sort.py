def selection_sort(arr):
    N = len(arr)
    for i in range(N - 1):
        min_index = i
        for j in range(i + 1, N):
            if arr[j] < arr[min_index]:  # Check if current element is smaller than the current minimum
                min_index = j
        # Swap only if a new minimum was found
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [30, 20, 10, 60, 25, 50]
print(selection_sort(arr))
