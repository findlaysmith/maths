def fib_gen():
  fib = [0, 1]
  print(fib[0])
  print(fib[1])
  while True:
    w = fib[(len(fib)-1)] + fib[(len(fib)-2)]
    fib.append(w)
    print(w)

def is_fib(val):
  fib = [0, 1]
  for w in fib:
    if val == w:
      print("%s is a fibonacci number" % val)
      break
  while True:
    w = fib[(len(fib)-1)] + fib[(len(fib)-2)]
    fib.append(w)
    if val == w:
      print("%s is a fibonacci number" % val)
      break
    if w > val:
      print("%s is not a fibonacci number" % val)
      break

def fib_pos(val):
  fib = [0, 1]
  n = 2
  while True:
    w = fib[(len(fib)-1)] + fib[(len(fib)-2)]
    fib.append(w)
    n = n + 1
    if val == w and 10 < val < 20:
      print(str(val) + " is the " + str(n) + "th fibonacci number.")
      break
    elif val == w and str(val)[int(len(str(val)) -1)] == 1:
      print(str(val) + " is the " + str(n) + "st fibonacci number.")
      break
    elif val == w and str(val)[len(str(val)) - 1] == 2:
      print(str(val) + " is the " + str(n) + "nd fibonacci number.")
      break
    elif val == w and str(val)[len(str(val))-1] == 3:
      print(str(val) + " is the " + str(n) + "rd fibonacci number.")
      break
    elif val == w:
      print(str(val) + " is the " + str(n) + "th fibonacci number.")
      break
    if w > val:
      print(str(val) + " is not a fibonacci number.")
      break
