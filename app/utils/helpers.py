import json
import logging
import kubernetes
from .nodepool import NodePool

def get_nodepools():
  api = kubernetes.client.CustomObjectsApi()
  nodepools = api.list_cluster_custom_object(group="cluster.trojanekkk.com", version="v1", plural="nodepools")['items']

  if (len(nodepools) == 0):
    logging.warning("No NodePools found")
    return 0
  
  nodepools_obj = [ NodePool(np['metadata']['name'], np['spec']['selectors'], np['spec']['taints']) for np in nodepools ]

  logging.info(f"Found the following NodePools in the cluster: {nodepools_obj}")

  return nodepools_obj


def get_owners(node, nodepools):
  owners = []
  for np in nodepools:
    if (np.check_ownership(node)):
      owners.append(np)

  return owners

def taint_node(node, owners):
  api = kubernetes.client.CoreV1Api()

  node_config = api.read_node(node.name)
  taints = node_config.spec.taints if node_config.spec.taints else []

  new_taints = []
  for owner in owners:
    new_taints.extend(owner.taints)

  for taint in taints:
    if taint.key not in [t['key'] for t in new_taints]:
      new_taints.append(taint)

  body = {
    "spec": {
      "taints": new_taints
    }
  }

  print(body)

  logging.info(f"Applying the following parameters: {body} to Node {node}")

  try:
    api.patch_node(node.name, body)
    logging.info(f"Successfully tainted Node {node}")
  except kubernetes.client.exceptions.ApiException as e:
    logging.error(f"Exception when patching Node: {e}")
