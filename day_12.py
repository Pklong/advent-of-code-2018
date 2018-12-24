from time import time
start = time()
with open('input_12.txt') as input_file:
  initial_state = input_file.readline().strip()
  negative_plants = 0
  rules = {}
  states = set()
  for line in input_file:
    if line == '\n':
      continue
    state, affect = line.split(' => ')
    rules[state] = affect.strip()
  plants = list(initial_state.split(': ')[1])
  generations = []
  for step in range(100):
    #print("GRAND TOTAL:", grand_total)
    new_plants = ['.', '.']
    negative_plants += 2
    for i in range(len(plants)):
      plant_rule = ''.join(plants[i - 2: i + 3])
      if i == 1:
        plant_rule = '.' + ''.join(plants[i - 1: i + 3])
      if i == 0:
        plant_rule = '..' + ''.join(plants[i: i + 3])
      if i == len(plants) - 1:
        plant_rule = ''.join(plants[i - 2: i + 1]) + '..'
      if i == len(plants) - 2:
        plant_rule = ''.join(plants[i - 2: i + 2]) + '.'
      new_plants.append(rules[plant_rule])
    plants = new_plants + ['.', '.']
    
    total = 0
    
    for j in range(len(plants)):
      if plants[j] == '#':
        total += j - negative_plants        
    
    if len(generations):
      prev = generations[-1]
      #print("Previous:", prev)
      #print("Current:", total)
      diff = total - prev
      #print(total)
      #print("Difference:", diff)
      if diff in states:
        #print("REPEAT:")
        #print(diff)
        #print("ON TURN", step)
        #break
        pass
      else:
        states.add(diff)
    generations.append(total)
  smaller = 50000000000 - 100
  print((smaller * 81) + generations[-1])
  

  
      
      
      
  
print("Time: ", time() - start)
