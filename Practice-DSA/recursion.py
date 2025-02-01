# def value(n):
#     if n >= 0:
#         value(n-1)
#         print(n, end=" ")
# value(10)


# def value(n):
#     if n >= 0:
#         print(n, end=" ")
#         value(n-1)
# value(10)

def value(n):
    if n > 0:
        value(n-1)
        print(2*n, end=" ")
             
value(5)
