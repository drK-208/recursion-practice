def factorial(n):
  '''Compute the factorial of n'''
  if n - 1 == 0:
    return n
  else:
    return n * factorial(n - 1)

def sumList(L):
  '''Calculates the sum of a list of numbers.'''
  if [] == L:
    return 0
  else:
    return L[0] + sumList(L[1:])

def fib(n):
  '''Calculates the fibonacci number n.'''
  if n == 1 or n == 2:
    return 1
  else:
   return fib(n - 1) + fib(n - 2)

def ind(e, L):
  '''Takes in element e and list L and returns the index at which e is first found 
  in L. If e is not in L then return the length of the list.'''
  if len(L) == 0:
    return 0
  elif e == L[0]:
    return 0
  else:
    return 1 + ind(e, L[1:])
