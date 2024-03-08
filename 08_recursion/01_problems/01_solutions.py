def printN(n):
        if n > 0:
            printN(n-1)
            print(n, end=' ')


def printNReverse(n):
        if n > 0:
            print(n, end=' ')
            printNReverse(n-1)

def printNOdd(n):
      if n > 0:
            printNOdd(n-1)
            print(2*n-1, end=' ')

def printNEven(n):
      if n > 0:
            printNEven(n-1)
            print(2*n, end=' ')

def printNOddReverse(n):
      if n > 0:
            print(2*n-1, end=' ')
            printNOddReverse(n-1)

def printNEvenReverse(n):
      if n > 0:
            print(2*n, end=' ')
            printNEvenReverse(n-1)
            
    
printN(10)
print()
printNReverse(10)
print()
printNOdd(10)
print()
printNEven(10)
print()
printNOddReverse(10)
print()
printNEvenReverse(10)