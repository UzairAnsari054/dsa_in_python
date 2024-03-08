# Rules:
# 1. Assume that the problem is solved by figuring the way to solve it by passing in small values
# 2. Make the recursive case (n-1)
# 3. Make a base case (if n==0 then stop)

def printNSum(n):
      if n == 0:
            return 0
      else:
            return n + printNSum(n-1)
      
def printNSumOdd(n):
      if n == 0:
            return 0
      else:
            return 2*n-1 + printNSumOdd(n-1)
      
def printNSumEven(n):
      if n == 0:
            return 0
      else:
            return 2*n + printNSumEven(n-1)
      
def printNFactorial(n):
      if n == 1:
            return 1
      else:
            return n * printNFactorial(n-1)

def printNSquare(n):
      if n == 0:
            return 0
      else:
            return n*n + printNSquare(n-1)
      
print(printNSum(5))
print()
print(printNSumOdd(10))
print()
print(printNSumEven(10))
print()
print(printNFactorial(5))
print()
print(printNSquare(5))