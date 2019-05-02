def getFunctionValue(x):
  return x * x - 3

def getMiddleValue(a, b):
  return (a + b) / 2

def printInfo():
  print("a : " + str(a))
  print("b : " + str(b))
  print("c : " + str(c))
  print("f(c) : " + str(getFunctionValue(c)))
  print("===================================")

a = 1.0
b = 2.0
c = 0
learning_rate = 0.01

while (True):
  temp = c
  c = getMiddleValue(a, b)
  printInfo()

  if (getFunctionValue(c) < 0):
    a = c
  else:
    b = c

  if (abs(temp - c) < learning_rate and getFunctionValue(c) < learning_rate):
    print("approximation root : " + str(temp))
    break