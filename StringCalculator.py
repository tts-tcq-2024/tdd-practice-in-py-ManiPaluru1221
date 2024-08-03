#import re

def func(input):
  delim = ','
  if(input[0] == '/'):
    ind = input.find('\n')
    delim = input[2:ind+1]
    input = input[ind+1:]
    if len(delim) > 0:
      delim = delim[1:len(delim)-1]
  return delim, input

def add(input):
  if(input == "" or input == "0"):
    return 0
  delim, input = func(input)
  #numbers = input.split([delim, '\n'])
  #numbers = re.split(r',|\n', my_str_2)
  numbers = input.replace(delim, '\n').split('\n')
  sum = 0
  for item in numbers:
    if int(item) >= 1000:
      continue
    sum += int(item)
  return sum
