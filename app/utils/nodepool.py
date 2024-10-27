class NodePool:
  def __init__(self, name, selectors, taints):
    self.name = name
    self.selectors = selectors
    self.taints = taints

  def __str__(self):
    return self.name

  def __repr__(self):
    return self.name
  
  def check_ownership(self, node):
    if ('matchLabels' in self.selectors):
      for label in node.labels:
        if (label in self.selectors['matchLabels']):
          return True
      
    if ('matchAnnotations' in self.selectors):
      for annotation in node.annotations:
        if (annotation in self.selectors['matchAnnotations']):
          return True
      
    return False