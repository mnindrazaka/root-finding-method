def getFunctionValue(x):
  return (x * x * x) + (3 * x) - 5
  # return 3 * x - 21

def getSecant(a, b):
  return a - (b - a) * getFunctionValue(a) / (getFunctionValue(b) - getFunctionValue(a))

def printInfo():
  print("a : " + str(a))
  print("b : " + str(b))
  print("x : " + str(x))
  print("f(x) : " + str(getFunctionValue(x)))
  print("===================================")

a = 1
b = 2

x = 0
accuracy = 0.001

while (True):
  x = getSecant(a, b)
  printInfo()

  if (getFunctionValue(x) < 0):
    a = x
  else:
    b = x

  if (abs(getFunctionValue(x)) <= accuracy):
    print("approximation root : " + str(x))
    break