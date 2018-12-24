class Node:
  def __init__(self, child_count, medi_count):
    self.child_count = child_count
    self.medi_count = medi_count
    self.value = 0
    self.children = []
    self.id = "{0}-{1}".format(child_count, medi_count)

  def __repr__(self):
    return self.id

def build_tree(data):
  if not len(data):
    print('no more info')
    return
  if data[0]:
    # have children
    node = Node(data[0], data[1])
    for c in range(data[0]):
      node.children.append(build_tree(data[2:]))
    return node
  else:
    # no children
    node = Node(data[0], data[1])
    for m in range(1, data[1] + 1):
      node.medidata.append(data[m])
    return node
      
with open('input_8.txt') as input_file:
  nums = input_file.read().split(' ')
  nums = [int(n) for n in nums]
  stack = []
  medidata = 0
  root = None
  while len(nums):
    #print("STACK: ", stack)
    #print("NUMS: ", nums)
    #print("MEDIDATA COLLECTED: ", medidata)
    c_count, m_count = nums[:2]
    #print("CHILD COUNT, {0}, MEDI COUNT {1}".format(c_count, m_count))
    nums = nums[2:]
    node = Node(c_count, m_count)
    if not root:
      root = node
    if not node.child_count:
      #print("ADDING TO TOTAL MEDIDATA")
      # add leaf medidata
      for i in range(m_count):
        medidata += nums[i]
        node.value += nums[i]
      #print("MEDIDATA IS NOW: {0}".format(medidata))
      
      nums = nums[m_count:]
      #print("NUMS IS NOW: {0}".format(nums))      
      # reduce parent's children count
      parent = stack.pop()
      parent.child_count -= 1
      parent.children.append(node)
      #print("PARENT'S CHILDREN EXHAUSTED")
      while not parent.child_count:
        if not len(nums):
          break
        #print("ADDING PARENT MEDIDATA")
        for i in range(parent.medi_count):
          #medidata += nums[i]
          index = nums[i]
          if index == 0:
            continue
          elif index > len(parent.children):
            continue
          else:
            parent.value += parent.children[index - 1].value
        #print("MEDIDATA IS NOW: {0}".format(medidata))        
        nums = nums[parent.medi_count:]
        #print("NUMS IS NOW: {0}".format(nums))      
        if len(stack):
          stack[-1].children.append(parent)
          parent = stack.pop()
          parent.child_count -= 1
      if parent.child_count:
        stack.append(parent)
    else:
      if not len(nums):
        break
      #print("ADDING PARENT {0}".format(node))
      stack.append(node)
      
  #print(medidata)
  #print(stack)
  #print(nums)
  print(root.value)
  
