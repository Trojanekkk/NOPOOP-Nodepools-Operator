# :no_entry_sign: :poop: NO POOP (NOdePOols OPerator)

## Usage

### kubectl

1. Apply CRDs to the cluster
```bash
kubectl apply -f https://raw.githubusercontent.com/Trojanekkk/NOPOOP-Nodepools-Operator/refs/heads/main/k8s/crd.yaml
```

2. Deploy a NOPOOP
```bash
kubectl apply -f https://raw.githubusercontent.com/Trojanekkk/NOPOOP-Nodepools-Operator/refs/heads/main/k8s/deployment.yaml
```

3. Create a NodePool resource
```bash
kubectl apply -f << EOF
  apiVersion: cluster.trojanekkk.com/v1
  kind: NodePool
  metadata:
    name: apps
  spec:
    selectors:
      matchLabels:
        pool: apps
    taints:
    - key: "node-role"
      value: "apps"
      effect: "NoSchedule"
EOF
```

4. (Re)Add nodes to your cluster



### helm
1. Apply CRDs to the cluster

2. Deploy the operator to the cluster

3. Specify NodePools for your cluster

4. (Re)Add nodes to the cluster

## Usage