with open('input_3.txt') as input_file:
  grid = [[ 0 for i in range(1000)] for j in range(1000)]
  good_claim = None
  for line in input_file:
    line = line.strip().split(' ')
    start_x, start_y = line[2].split(',')
    width, tall = line[3].split('x')
    start_x = int(start_x)
    start_y = int(start_y[:-1])
    width = int(width)
    tall = int(tall)
    for i in range(start_x + 1, start_x + width + 1):
      for j in range(start_y + 1, start_y + tall + 1):
        grid[j][i] += 1
  total = 0

  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[j][i] > 1:
        total += 1
  print(total)
  
with open('input_3.txt') as input_file:
  good_claim = None
  for line in input_file:
    line = line.strip().split(' ')
    claim_id = line[0]
    start_x, start_y = line[2].split(',')
    width, tall = line[3].split('x')
    start_x = int(start_x)
    start_y = int(start_y[:-1])
    width = int(width)
    tall = int(tall)
    take = True
    for i in range(start_x + 1, start_x + width + 1):
      if not take:
        break
      for j in range(start_y + 1, start_y + tall + 1):
        if grid[j][i] != 1:
          take = False
          break
    if take:
      print(claim_id)

        
