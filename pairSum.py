arr = [70, 11, 7, 15, 2]
target = 9


#Brute-force approch
# for i in range(0, len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] + arr[j] == target:
#             print(i, j)
    
for num in arr:
    needVlaue = target-num
    if needVlaue in arr:
        print(arr.index(needVlaue), end= " ")