class Vertex:
  def __init__(self, id):
    self.id = id
    self.deps = []
    self.must_do = []
    self.seconds = (ord(id) - ord("A")) + 61

  def __eq__(self, o):
    return self.id == o.id

  def __gt__(self, o):
    return self.id > o.id

  def __repr__(self):
    return self.id

class Graph:
  def __init__(self):
    self.vertices = {}

  def add_vertex(self, vertex):
    self.vertices[vertex.id] = vertex

  def add_edge(self, v1, v2):
    self.vertices[v1.id].deps.append(v2)
    self.vertices[v2.id].must_do.append(v1)

  def has_vertex(self, v):
    if self.vertices.get(v.id, False):
      return True
    else:
      return False

  def get_vertex(self, v_id):
    return self.vertices.get(v_id, None)

  def get_vertices(self):
    return self.vertices.values()

with open('input_7.txt') as input_file:
  g = Graph()
  for line in input_file:
    words = line.split(' ')
    v, d = Vertex(words[1]), Vertex(words[-3])
    if not g.has_vertex(v):
      g.add_vertex(v)
    if not g.has_vertex(d):
      g.add_vertex(d)
    g.add_edge(g.get_vertex(v.id), g.get_vertex(d.id))
  result = []
  queue = []
  seen = {}
  for v in g.get_vertices():
    print(v.id, v.seconds)    
    if len(v.must_do) == 0:
      
      queue.append(v)


  queue.sort()
  seconds = 0
  workers = 5
  work_queue = []
  while queue or work_queue:
    #print("QUEUE:", queue)
    #print("WORK QUEUE:", work_queue)
    seconds += 1
   

    
    while workers and queue:
      node = queue.pop(0)
      if len(node.must_do):
        queue.insert(0, node)
        break
      else:
        work_queue.append(node)
        workers -= 1
    #print("CURRENT NODE: ", current_node)
    #print("DEPS: ", current_node.deps)
    #print("MUST DOS: ", current_node.must_do)
    for job in work_queue:
      job.seconds -= 1
      if not job.seconds:
        result.append(job.id)
        seen[job.id] = True
        workers += 1
        for v in job.deps:
          if v not in queue and v.id not in seen.keys() and v not in work_queue:
            queue.append(v)             
    work_queue = [job for job in work_queue if job.seconds]
    #result.append(current_node.id)

    firsties = []
    lasties = []
    for v in queue:
      for d in v.must_do:
        if seen.get(d.id, False):
          v.must_do.pop(v.must_do.index(d))
      if len(v.must_do) == 0:
        firsties.append(v)
      else:
        lasties.append(v)
    firsties.sort()
    lasties.sort()
    queue = firsties + lasties
    
    
      

  result = "".join(result)
  print(result)
  #print(len(result))
  print("SECONDS: ", seconds)

  

# IABCDEFGHJKLMNOPQRSVXYZ
# ITUWBDFGHJKNPVYAEOQMCRLSZX    
# IBDFGHJKNPTUVEWYAOMCQRLSZX      
# IBEGJRTDOUMWHLNXYQZ
# IBEGJRTDOUMORWGHLNOXYQRZ


# 439 low
# 1133 high
