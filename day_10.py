def has_neighbor(p, points):
  alts = [
    [p[0] + 1, p[1]],
    [p[0] - 1, p[1]],
    [p[0], p[1] + 1],
    [p[0], p[1] - 1]
    ]
  for point in points:
      if point in alts:
        return True
  return False

with open('input_10.txt') as input_file:
  positions = []
  velocities = []
  y_max, x_max = float('-inf'), float('-inf')
  y_min, x_min = float('inf'), float('inf')
  for line in input_file:
    pos_list = line.split('=<')
    pos = pos_list[1].split('>')[0]
    vel = pos_list[-1].split('>')[0]
    pos = [int(n) for n in pos.split(',')]
    vel = [int(n) for n in vel.split(',')]
    x, y = pos
    x_max = max(x_max, x)
    x_min = min(x_min, x)
    y_max = max(y_max, y)
    y_min = min(y_min, y)
    positions.append(pos)
    velocities.append(vel)
  print(x_max, y_max)
  print(x_min, y_min)
  
  
  steps = 0
  grid = [[" " for i in range(200)] for i in range(200)]
  for i in range(10880):
    y_max, x_max = float('-inf'), float('-inf')
    y_min, x_min = float('inf'), float('inf')

    #steps += 1
    for i in range(len(positions)):
      pos, vel = positions[i], velocities[i]
      pos[0] += vel[0]
      pos[1] += vel[1]
      x, y = pos
      x_max = max(x_max, x)
      x_min = min(x_min, x)
      y_max = max(y_max, y)
      y_min = min(y_min, y) 
    #print("STEP", steps)
    # neighbor_count = 0
    # for point in positions:
    #   if has_neighbor(point, positions):
    #     neighbor_count += 1
    # print("STEP", steps)
    # print("NEIGHBORS: ", neighbor_count)
  f = open('result.txt', 'w')
  positions = ['{0}, {1}'.format(pos[0], pos[1]) for pos in positions]
  result_string = '\n'.join(positions)
  f.write(result_string)
    
    
    # positions_dup = [[pos[0] + abs(x_min), pos[1] + abs(y_min)] for pos in positions]
    # grid = [[" " for i in range(x_max + abs(x_min) + 1)] for i in range(y_max + abs(y_min) + 1)]


    # grid_dup = grid.copy()
    # print("DONE")
    # for pos in positions_dup:
    #   x, y = pos
    #   grid_dup[y][x] = '#'
    # for row in grid:
    #   print("".join(row))
      

  
