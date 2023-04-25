equation1 = input("Enter equation 1: ")
equation2 = input("Enter equation2: ")
equation1 = equation1.replace("-", "+-").split("x+")
secondhalf = equation1[1]
del equation1[1]
secondhalf = secondhalf.split("y=")
equation1.append(secondhalf[0])
equation1.append(secondhalf[1])
try:
  equation1[0] = equation1[0].replace("+", "")
except:
  pass
try:
  equation1[1] = equation1[1].replace("+", "")
except:
  pass
try:
  equation1[2] = equation1[2].replace("+", "")
except:
  pass
equation2 = equation2.replace("-", "+-").split("x+")
secondhalf2 = equation2[1]
del equation2[1]
secondhalf2 = secondhalf2.split("y=")
equation2.append(secondhalf2[0])
equation2.append(secondhalf2[1])
try:
  equation2[0] = equation2[0].replace("+", "")
except:
  pass
try:
  equation2[1] = equation2[1].replace("+", "")
except:
  pass
try:
  equation2[2] = equation2[2].replace("+", "")
except:
  pass
if equation1[0] == "":
  equation1[0] = 1
elif equation1[0] == "-":
  equation1[0] = -1
if equation1[1] == "":
  equation1[1] = 1
elif equation1[1] == "-":
  equation1[1] = -1
if equation2[0] == "":
  equation2[0] = 1
elif equation2[0] == "-":
  equation2[0] = -1
if equation2[1] == "":
  equation2[1] = 1
elif equation2[1] == "-":
  equation2[1] = -1
equation1[0] = int(equation1[0])
equation1[1] = int(equation1[1])
equation1[2] = int(equation1[2])
equation2[0] = int(equation2[0])
equation2[1] = int(equation2[1])
equation2[2] = int(equation2[2])
yfound = False
while not yfound:
  if equation1[0] == -equation2[0]:
    equation2[0] = equation1[0] + equation2[0]
    equation2[1] = equation1[1] + equation2[1]
    equation2[2] = equation1[2] + equation2[2]
    equation2[2] = equation2[2] / equation2[1]
    equation2[1] = equation2[1] / equation2[1]
    equation1[2] = equation1[2] + equation2[2] * -1 * equation1[1]
    equation1[1] = equation1[1] + equation2[1] * -1 * equation1[1]
    equation1[2] = equation1[2] / equation1[0]
    equation1[0] = equation1[0] / equation1[0]
    yfound = True
    print(equation1)
    print(equation2)
  else:
    b = (-1 * equation2[0] / equation1[0])
    equation1[0] = equation1[0] * b
    equation1[1] = equation1[1] * b
    equation1[2] = equation1[2] * b
