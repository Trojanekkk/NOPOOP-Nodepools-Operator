import kopf
import logging
from utils.node import Node
from utils import helpers

@kopf.on.create('node')
def create_fn(body, **kwargs):

  node = Node(body)

  logging.info(f"Node {node} created")

  if (len(node.labels) == 0 and len(node.annotations) == 0):
    logging.warning("No labels or annotations")
    logging.warning(f"Skipping the Node {node}...")
    return 0

  nodepools = helpers.get_nodepools()

  owners = helpers.get_owners(node, nodepools)

  if (len(owners) == 0):
    logging.warning(f"Node does not belong to any NodePool")
    logging.warning(f"Skipping the Node {node}...")
    return 0
  
  logging.info(f"Assigning Node {node} to the following NodePool(s): {owners}")

  helpers.taint_node(node, owners)

  