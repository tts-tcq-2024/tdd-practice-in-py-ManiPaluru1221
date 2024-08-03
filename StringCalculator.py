def add(input):
  if(input[0] == '/'):
    ind = input.find('\n')
    delim = input[2:ind+1]
    input = input[ind+1:]
    if delim.length() > 0:
      delim.erase(0,1)
      delim.erase(delim.length()-1,1)
  else:
    delim = ','
  sum = 0
  numbers = input.split([delim, '\n'])
  
  for item in numbers:
    if int(item) >= 1000:
      continue
    sum += int(item)
  return sum
