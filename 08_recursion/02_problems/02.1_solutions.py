def sumN(n):
    if n == 0:
        return 0
    else:
        return n + sumN(n-1)
    
def sumNodd(n):
    if n == 0:
        return 0
    else:
        return 2*n - 1 + sumNodd(n-1)
    
def sumNeven(n):
    if n == 0:
        return 0
    else:
        return 2*n + sumNeven(n-1)
    
def sumNFactorial(n):
    if n == 1:
        return 1
    else:
        return n * sumNFactorial(n-1)
    
def sumNSquare(n):
    if n == 0:
        return 0
    else: 
        return n*n + sumNSquare(n-1)

print(sumN(5))
print(sumNodd(5))
print(sumNeven(5))
print(sumNFactorial(5))
print(sumNSquare(5))