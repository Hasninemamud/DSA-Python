def missingNumber(arr):
    sort_arr = sorted(arr)
    n = len(sort_arr)
    if arr[n-1] == 1:
        return 2
    else:
        for i in range(1,n+1):
            for j in sort_arr:
                if i not in sort_arr:
                    return i
                else:
                    i += 1
   
arr = [2, 1]     
mi = missingNumber(arr)          
print(mi)      
        
        
        