# sample spark-cluster on the kubernetes

## environment settings

you set the mount path. (use absolute path!!!)

```spark-cluster.yaml
      volumes:
        - name: mount-directory
          hostPath:
            path: <path> ## mount-path
```

## deploy and run clusters

```shell
kubectl apply -f ./spark-cluster.yml
```

## delete resources

```shell
kubectl delete -f ./spark-cluster.yml
```

## show logs

```shell
kubectl get pods
```

```shell
kubectl logs <pods-name>
```
