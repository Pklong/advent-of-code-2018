from collections import deque

with open('input_9.txt') as input_file:
  file = input_file.read().split(' ')
  num_players, last_marble = int(file[0]), int(file[-2])
  last_marble *= 100
  player = -1
  #game = [0]
  game = deque([0])
  #num_players, last_marble = 10, 1618
  #num_players, last_marble = 13, 7999
  #num_players, last_marble = 17, 1104
  #num_players, last_marble = 21, 6111
  
  players = [0 for i in range(num_players)]  
  for turn in range(1, last_marble + 1):
    #print("GAME: ", game)
    #print("TURN: ", turn)
    #print()
    player += 1
    player %= len(players)
    #print("CURRENT PLAYER: ", player)
    
    if turn % 23 == 0:
      game.rotate(7)
      players[player] += game.pop() + turn
      game.rotate(-1)
    else:
      game.rotate(-1)
      game.append(turn)
  print(max(players))

