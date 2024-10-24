# #sum of first N natural numbers

# def sumOfN(N):
#     if N == 1:
#         return 1
#     return N+sumOfN(N-1)
# print(sumOfN(5))

# #sum of first N natural numbers

# def sumOfNodd(N):
#     if N == 1:
#         return 1
#     return  2*N-1 + sumOfNodd(N-1)
# print(sumOfNodd(5))

# #sum of first N even natural numbers

# def sumOfNeven(N):
#     if N == 1:
#         return 2
#     return  2*N + sumOfNeven(N-1)
# print(sumOfNeven(10))

# #Factorial number

# def factorialnum(N):
#     if N == 0:
#         return 1
#     return N * factorialnum(N-1)
# print(factorialnum(5))


#square N natural number

# def squareN(N):
#     if N == 1:
#         return 1
#     return N*N + squareN(N-1)
# print(squareN(5))

def sumNat(N):
    if N == 0 :
        return 0
    return N + sumNat(N-1)
print(sumNat(5))
    