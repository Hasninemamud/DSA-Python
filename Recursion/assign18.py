def printN(n):
    if n > 0:
        printN(n-1)
        print(n, end=" ")
        
def printNrev(n):
    if n > 0:
        print(n, end=" ")
        printNrev(n-1)
        
#Odd netural number

def printNoddNums(n):
    if n > 0:
        printNoddNums(n-1)  #10-1,9-1,8-1,7-1,6-1,5-1,4-1,3-1,2-1,1
        print(2*n-1, end=" ")

#even number
def printNevenNums(n):
    if n > 0:
        printNevenNums(n-1) 
        print(2*n, end=" ")
     
        
# printN(5)
printNevenNums(10)