class Node:
  def __init__(self, body):
    metadata = body['metadata']
    self.name = metadata['name']

    if ('labels' in metadata):
      self.labels = metadata['labels']
    else:
      self.labels = {}

    if ('annotations' in metadata):
      self.annotations = metadata['annotations']
    else:
      self.annotations = {}

  def __str__(self):
    return f"{self.name} (labels: {self.labels}, annotations: {self.annotations})"
  
  