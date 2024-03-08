# 1,2,3,4....n
def printN(n):
    if n > 0:
        printN(n-1)
        print(n, end=' ')

def printNreverse(n):
    if n > 0:
        print(n, end=' ')
        printNreverse(n-1)

def printNodd(n):
    if n > 0:
        printNodd(n-1)
        print(2*n - 1, end=' ')

def printNeven(n):
    if n > 0:
        printNeven(n-1)
        print(2*n, end=' ')

def printNoddreverse(n):
    if n > 0:
        print(2*n -1, end=' ')
        printNoddreverse(n-1)

def printNevenreverse(n):
    if n > 0:
        print(2*n, end=' ')
        printNevenreverse(n-1)

printN(10)
print()
printNreverse(10)
print()
printNodd(10)
print()
printNeven(10)
print()
printNoddreverse(10)
print()
printNevenreverse(10)