def getFunctionValue(x):
  return x * x - 27

def printInfo(x):
  print("x  : " + str(x))
  print("fx : " + str(getFunctionValue(x)))
  print("=================================")

a = 5.0
b = 6.0
n = 10
step = (b - a) / n

for i in range(0, n):
  currentValue = a + step * i
  nextValue = currentValue + step

  printInfo(currentValue)
  fx1 = getFunctionValue(currentValue)
  fx2 = getFunctionValue(nextValue)

  if (fx1 * fx2 < 0):
    printInfo(nextValue)
    print("Hasil berada dintara " + str(currentValue) + " dan " + str(nextValue))
    break