from sys import argv

dirs = {
  "\\s": "l",
  "\\w": "r",
  "\\n": "l",
  "\\e": 'r',
  "/e": "l",  
  "/w": "l",
  "/n": "r",
  "/s": "r"
}

def sort_carts(carts):
  sorted = False
  while not sorted:
    sorted = True
    for i in range(len(carts) - 1):
      if carts[i].pos[1] > carts[i + 1].pos[1]:
        carts[i], carts[i + 1] = carts[i + 1], carts[i]
        sorted = False
      elif carts[i].pos[1] == carts[i + 1].pos[1] and carts[i].pos[0] > carts[i + 1].pos[0]:
        carts[i], carts[i + 1] = carts[i + 1], carts[i]
        sorted = False
        
class Cart:
  def __init__(self, direction, pos):
    self.direction = direction
    self.pos = pos
    self.rotation = ['<', '|', '>']
    self.crashed = False

  def __eq__(self, oc):
    return self.pos == oc.pos

    
  def __repr__(self):
    return repr((self.direction, self.pos, self.rotation))

  def rotate(self):
    self.rotation = [*self.rotation[1:], self.rotation[0]]
    
  def handle_turn(self, grid):
    grid_value = grid[self.pos[1]][self.pos[0]]
    turn = dirs.get(grid_value + self.direction[0], None)
    
    if turn == 'l':
      self.direction = [self.direction[-1], *self.direction[:-1]]
    if turn == 'r':
      self.direction = [*self.direction[1:], self.direction[0]]
      
    if grid_value == '+':
      if self.rotation[0] == '<':
        self.direction = [self.direction[-1], *self.direction[:-1]]
      if self.rotation[0] == '>':
        self.direction = [*self.direction[1:], self.direction[0]]
      self.rotate()

  def move(self, grid):
    x, y = self.pos
    if self.direction[0] == 's':      
      self.pos = [x, y + 1]
    if self.direction[0] == 'n':     
      self.pos = [x, y - 1]
    if self.direction[0] == 'w':
      self.pos = [x - 1, y]
    if self.direction[0] == 'e':
      self.pos = [x + 1, y]
  
with open(argv[1]) as input_file:
  carts = []
  grid = []
  for idx, line in enumerate(input_file):
    line = line[:-1] # newline
    grid.append(list(line))
    if ">" in line:
      loc = [line.index('>'), idx]
      cart = Cart(['e', 's', 'w', 'n'],  loc)
      carts.append(cart)
      grid[loc[1]][loc[0]] = '-'
    if "<" in line:
      loc = [line.index('<'), idx]
      cart = Cart(['w', 'n', 'e', 's'],  loc)      
      carts.append(cart)      
      grid[loc[1]][loc[0]] = '-'     
    if "^" in line:
      loc = [line.index('^'), idx]
      cart = Cart(['n', 'e', 's', 'w'],  loc)
      carts.append(cart)      
      grid[loc[1]][loc[0]] = '|'      
    if "v" in line:
      loc = [line.index('v'), idx]
      cart = Cart(['s', 'w', 'n', 'e'],  loc)      
      carts.append(cart)
      grid[loc[1]][loc[0]] = '|'

  crashed = None
  step = 0
  while len(carts) != 1:
    cart_positions = []
    sort_carts(carts)
    for cart in carts:
      cart.move(grid)
      cart.handle_turn(grid)
      for ac in carts:
        if ac is cart:
          continue
        elif ac.pos == cart.pos:
          ac.crashed = True
          cart.crashed = True
          print(ac, "CRASHED", cart)
          carts = [c for c in carts if not c.crashed]
  print(carts)
              

