def manhattan_distance(c1, c2):
  return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])

with open('input_6.txt') as input_file:
  x_min, y_min = float('inf'), float('inf')
  x_max, y_max = float('-inf'), float('-inf')
  coords = []
  dimension = {}
  for line in input_file:
    x, y = line.split(', ')
    x, y = int(x), int(y)
    coords.append((x, y))
    dimension[(x, y)] = 0
    x_min = min(x_min, x)
    y_min = min(y_min, y)
    x_max = max(x_max, x)
    y_max = max(y_max, y)
  grid = [[[float('inf'), None] for i in range(0, x_max + 2)] for j in range(0, y_max + 2)]



  
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      tote = 0
      for c in coords:
        #c_dist = manhattan_distance(c, (col, row))
        tote += manhattan_distance(c, (col, row))
        if tote < 10000:
          grid[row][col] = 1
        else:
          grid[row][col] = 0
  size_queen = 0
  for row in grid:
    for col in row:
      size_queen += col
  print(size_queen)
          #print("Distance from {0} to {1} is {2}".format(c, (row, col), c_dist))
        # dist, coord = grid[row][col]
  #       if not coord:
  #         grid[row][col] = [c_dist, c]
  #       if c_dist == dist and c != coord:
  #         grid[row][col] = [c_dist, '#']
  #       if c_dist < dist:
  #         grid[row][col] = [c_dist, c]
  # for row in grid:
  #   #print([a[1] for a in row])
  #   for col in row:
  #     if col[1] == '#' or col[1][0] <= x_min or col[1][0] >= x_max or col[1][1] <= y_min or col[1][1] >= y_max:
  #       continue
  #     else:
  #       dimension[col[1]] += 1
  #areas = list(dimension.values())
  #areas.sort()
  #print(areas)
            
# 5475 too high
