def sumassion(n):
    if n == 1:
        return 1
    else:
        return n + sumassion(n-1)
print(sumassion(5))