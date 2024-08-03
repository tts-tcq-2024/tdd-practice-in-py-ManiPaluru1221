def func(input):
  delim = ','
  if(input[0] == '/'):
    ind = input.find('\n')
    delim = input[2:ind+1]
    input = input[ind+1:]
    if len(delim) > 0:
      delim.erase(0,1)
      delim.erase(len(delim)-1,1)
  return delim

def add(input):
  if(input == "" or input == "0"):
    return 0
  delim = func(input)
  numbers = input.split([delim, '\n'])
  sum = 0
  for item in numbers:
    if int(item) >= 1000:
      continue
    sum += int(item)
  return sum
