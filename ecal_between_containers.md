# eCAL for distributing data between two containers

Create a new podman network with DNS resolution enabled:

```shell
podman network create shared_net
```

Adapt the [shift2sdv_manifest.yaml](./shift2sdv_manifest.yaml) and add workload configuration for the built containers:

```yaml
  ecal_example_publisher:
    runtime: podman
    agent: hpc1
    restartPolicy: NEVER
    runtimeConfig: |
      image: ghcr.io/eclipse-sdv-hackathon-chapter-two/shift2sdv/ecal_example_publisher:latest
      commandOptions: [ "--net=shared_net" ]
  ecal_example_subscriber:
    runtime: podman
    agent: hpc1
    restartPolicy: NEVER
    runtimeConfig: |
      image: ghcr.io/eclipse-sdv-hackathon-chapter-two/shift2sdv/ecal_example_subscriber:latest
      commandOptions: [ "--net=shared_net" ]
```

**Note:** To run your current Ankaios manifest later inside the test vehicle, please revert the `--net=shared_net` to `--net=host`.

Start the Ankaios cluster:

```shell
restart-shift2sdv
```

Check the logs of the `ecal_example_subscriber` by running:

```shell
ank-logs ecal_example_subscriber
```

You should see messages arriving.

Stop the Ankaios cluster:

```shell
stop-shift2sdv
```
