from time import time

def process(point, serial):
  rack_id = point[0] + 10
  power_level = rack_id * point[1]
  power_level += serial
  power_level *= rack_id
  if power_level > 99:
    power_level = int(list(str(power_level))[-3])
  else:
    power_level = 0
  return power_level - 5

def main():
  with open('input_11.txt') as input_file:
    grid = [[(i, j) for i in range(1, 301)] for j in range(1, 301)]
    grid_serial = int(input_file.read())
    #grid_serial = 42
    process_grid = [[process((i, j), grid_serial) for i in range(1, 301)] for j in range(1, 301)]

    #grid_serial = 18
    # power_point = None
    # powerful_grid = None
    # for row in range(len(grid) - 3):
    #   for col in range(len(grid[0]) - 3):
    #     sub_grid_total = 0
    #     grid_point = (col + 1, row + 1)
    #     for y in range(row, row + 3):
    #       for x in range(col, col + 3):
    #         sub_grid_total += process_grid[y][x]
            
    #     if not powerful_grid or powerful_grid < sub_grid_total:
    #       power_point = grid_point
    #       powerful_grid = sub_grid_total
    # print("POINT", power_point)
    # print("POWER", powerful_grid)
    power_point = None
    powerful_grid = None
    
    for row in range(len(grid)):
      for col in range(len(grid[0])):
        sum = process_grid[row][col]
        if (row - 1) > 0:
          sum += process_grid[row - 1][col]
        if (col - 1) > 0:
          sum += process_grid[row][col - 1]
        if (col - 1) > 0 and (row - 1) > 0:
          sum -= process_grid[row - 1][col - 1]
        process_grid[row][col] = sum

    size = 0
    biggest = None
    big_point = None
    target_size = None
    while size < 299:
      size += 1
      local_size = None
      local_point = None
      for row in range(300 - size):
        for col in range(300 - size):
          square_sum = process_grid[row][col] + process_grid[row + size][col + size] - process_grid[row][col + size] - process_grid[row + size][col]
          if not local_size or local_size < square_sum:
            local_point = (col + 2, row + 2)
            local_size = square_sum
      if not biggest or biggest < local_size:
        biggest = local_size
        big_point = local_point
        target_size = size
      # print("POINT IS", big_point)
      # print("BIGGEST IS", biggest)
      # print("IDEAL SIZE IS:",target_size)
      # print("CURRENT SIZE IS:", size)
    print(big_point)
    print(biggest)
    print(target_size)
        
if __name__ == '__main__':
  start = time()
  main()
  print(time() - start)
