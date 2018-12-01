from functools import reduce

# first star
with open('input_1.txt') as input_file:
  result = reduce(lambda x, y: x + int(y), input_file, 0)
  print(result)

# second start
with open('input_1.txt') as input_file:
  file_nums = input_file.read()[:-1]
  format_nums = [int(num) for num in file_nums.split('\n')]
  
  total = 0
  repeat = set([total])
  result = None
  
  while not result:
    for num in format_nums:
      total += num
      if total in repeat:
        result = True
        break
      else:
        repeat.add(total)
  print(total)
