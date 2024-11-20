# Forget the conventional - Shift to SDV

This repository provides a starter template for solving the "Forget the conventional - Shift to SDV" challenge using the following Eclipse SDV projects:
* [Ankaios](https://eclipse-ankaios.github.io/ankaios/latest/) - an embedded container and workload orchestrator targeted at automotive HPCs
* [eCAL](https://ecal.io/) – a fast communication middleware following the pub-sub principle
* [Symphony](https://github.com/eclipse-symphony/symphony/tree/main/docs) – a meta-orchestrator helping you manage your fleet from the cloud
* [Ankaios Dashboard](https://github.com/FelixMoelders/ankaios-dashboard) – a graphical user interface for the Ankaios orchestrator

The repo contains a pre-configured devcontainer that makes it easy for you to start developing and building container applications managed by Ankaios.

The container is designed to have an immediately running environment combined with a development environment for Ankaios workloads. Once triggered, all workloads are initially started and sample data is output.

## Links

- [Ankaios docs](https://eclipse-ankaios.github.io/ankaios/0.5/)
- [Ankaios Dashboard](https://github.com/FelixMoelders/ankaios-dashboard)
- [Ankaios quickstart](https://eclipse-ankaios.github.io/ankaios/0.5/usage/quickstart/)
- [eCAL docs](https://eclipse-ecal.github.io/ecal/)
- [Symphony docs](https://github.com/eclipse-symphony/symphony/tree/main/docs)
- [Podman](https://docs.podman.io/en/v4.9.3/)
- [What are devcontainers?](https://containers.dev/)

# Challenge

The challenge is to turn an ordinary vehicle into an innovation platform. To achieve this, two paths are available to the participants: the "Feature Path" and the "Connectivity Path". Both paths have different targets, yet combined showcase what a full-blown software-defined vehicle is capable of.

The following diagram shows the context view of the two paths:

![Context View](diagrams/context.drawio.svg)

## Feature Path

Unleash your creativity and develop innovative containerized applications managed by Ankaios using real data from the test vehicle.

Data is delivered via eCAL topics that your application subscribes to.

### GNSS

Subscribe to the eCAL topic `gps_data` within your custom application to receive live GPS data. More information about the data provided by the topic can be found [here](gnss_data.md).

### Vehicle dynamics

Subscribe to the eCAL topic `vehicle_dynamics` within your custom application to receive vehicle dynamics data from sensors such as speed, steering angle, and acceleration. More information about the data provided by the topic can be found [here](vehicle_dynamics.md).

### Object detection

Using the front camera of the test vehicle, an AI model runs object detection.

You can get the inference results by subscribing to the eCAL topic `object_detection`. More information on the data provided by the topic can be found [here](object_detection.md).

### Traffic sign detection

Using the front camera of the test vehicle, an AI model predicts the class ID of traffic signs.

You can get the inference results by subscribing to the eCAL topic `traffic_sign_detection`. More information on the data provided by the topic can be found [here](traffic_sign_detection.md).

### Web IVI

If you need an IVI to display information to the driver inside the test vehicle, there is one already prepared that can be extended. By default it is comment out inside the Ankaios manifest [shift2sdv_manifest.yaml](shift2sdv_manifest.yaml) and not started. See [here](web_ivi/README.md) for more information.

## Connectivity Path

Manage your fleet from the cloud turning feature upgrades into a seamless day-to-day business​.​

The connectivity path enables over-the-air updates and upgrades.

To enable this, write a [Symphony Provider application](apps/symphony_provider) that receives an Ankaios manifest via the Eclipse Symphony meta-orchestrator running on Azure. The received from the cloud manifest can be forwarded to Ankaios, which deploys all of the manifest's workloads. Running workloads are updated over-the-air by simply changing the image version of the containers to point to a different version of the application. 
New workloads listed in the manifest can upgrade the vehicle and add additional functionality.

The Symphony Provider can also be used to monitor the state of the Ankaios cluster and with this of the vehicle and report it to the cloud for auditing and debugging purposes.

# Development environment

The following is provided inside the devcontainer:

- Ankaios executables (`ank-server`, `ank-agent` and `ank`)

- Podman 4.9.3

- Pre-configured Ankaios startup config [shift2sdv_manifest.yaml](shift2sdv_manifest.yaml)

- Automation scripts (located in [scripts](/scripts)) for starting and stopping the demo of the challenge and debugging the developed applications. The development scripts are already added to the execution path of the devcontainer can be called from anywhere within the container:
    - [`restart-shift2sdv`](/scripts/restart-shift2sdv) builds all containers with the `build-apps` script, cleans up the system with `stop-shift2sdv` and starts everything again with `start-shift2sdv` 
    - [`build-apps`](/scripts/build-apps) triggers the Podman build of the developed hackathon applications. Just put your app in the [apps](/apps) folder to get it build too
    - [`stop-shift2sdv`](/scripts/stop-shift2sdv) cleans up the system by stopping Ankaios, cleaning up **all** Podman containers and cleaning up temporary files created for the Ankaios control interface
    - [`start-shift2sdv`](/scripts/start-shift2sdv) starts an Ankaios cluster with two agents ("hpc1" and "hpc2") and [shift2sdv_manifest.yaml](/shift2sdv_manifest.yaml) as a startup configuration
    - [`ank-logs`](/scripts/ank-logs) a wrapper around `podman logs` that helps you get the logs of a container using the ankaios workload name, e.g., `ank-logs symphony_provider`

## Vehicle data for development

Ask the Hack Coaches for eCAL test drive recordings to get real data for your application development. If a suitable recording is not available, the Hack Coaches can drive and record the explicit data you need.

Once you have obtained an eCAL recording, place the downloaded folder containing the eCAL recording in a `measurements/` folder that `git` ignores.

You can play it inside the devcontainer by running it:

```shell
ecal_play -m measurements/<ecal_recording_folder>
```

Start your application in another terminal window and check that it is receiving data.

For debugging, it might help to run the eCAL Monitor terminal UI `ecal_mon_tui` application inside your containerized application (if you have the eCAL binaries installed). This interactive terminal UI would display all eCAL topics with their content and metadata. The eCAL Monitor is always helpful for debugging, because if it does not see any data, it is very likely that your application is not receiving any data.

Debug your new application, assuming eCAL 5.12 is installed there (if you have already opened a shell inside your container, just skip this step):

```shell
podman run -it --rm --ipc=host --net=host --entrypoint /bin/bash <your_container_image> ecal_mon_tui
```

Start the eCAL Monitor terminal UI:

```shell
ecal_mon_tui
```

**Note:** Make sure to start the podman container receiving eCAL topic data with `--ipc=host`.

## Run devcontainer with VSCode

### Prerequisites
- [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) extension installed in VSCode

Open the subfolder containing this README file in VSCode:

```shell
code .
```

VSCode detects automatically that a `.devcontainer` folder exists inside this subfolder.
Please confirm the dialog to reopen VSCode inside the devcontainer.
Afterwards, open a new terminal inside the devcontainer in VSCode.

## Run devcontainer without VSCode

Navigate to the subfolder containing this README file and run the following command to build the devcontainer image:

```shell
docker build -t shift2sdv-dev:0.1 --target dev -f .devcontainer/Dockerfile .
```

Start the devcontainer with the required mount points:

```shell
docker run -it --privileged --name shift2sdv-dev -v <absolute/path/to>/challenge-shift-to-sdv:/workspaces/shift2sdv -p 25551:25551 --workdir /workspaces/shift2sdv shift2sdv-dev:0.1 /bin/bash
```

# Adding a new application

To add your new shiny application, just create a new folder under [apps](/apps) and add a Dockerfile that specifies the build and containerization steps. For an easy start you can also just copy one of the examples there and update it as you please :rocket:

The `build-apps` script is already configured to automatically build all apps located in the [apps](/apps).

For the application to also be executed by Ankaios, a configuration for it must either be:
* added to the initial startup manifest [shift2sdv_manifest.yaml](shift2sdv_manifest.yaml) or
* dynamically added during runtime via the control interface using the [Ankaios Python SDK](https://pypi.org/project/ankaios-sdk/)

You now only have to add your mighty code in :sparkler:

## Debugging your application

Although all new code is always perfect :sunglasses:, from time to time some debugging is quite helpful :nerd_face: 

The following steps will give you some directions how to get your hands on some useful logs:

### Getting the logs of your application

Testing out your application even before containerizing it is always the better choice, but sometimes you need to get some logs from the application running in the container. Podman already delivers strong tooling for this and to spare ourselves even more time, we wrapped the `podman logs` commands in a small script, which allows us to use the Ankaios workload name to get the logs by just calling:

```bash
ank-logs <your_app_name>
```

The command automatically follows the logs so you can get some :popcorn: and enjoy the show. If you get tired of it, you can always interrupt following the logs with a `ctrl + C`.

### Getting Ankaios logs

If you need some logs from Ankaios to get even deeper insights into the cluster, you can have a look in the `.logs` folder or follow the logs with the `tail -f <path to log>` command.

The following logs will be written by Ankaios in the `.logs` folder of the main repo:
* ank-server
* ank-agent-hpc1
* ank-agent-hpc2
* 

### Recordings

- Highway: https://we.tl/t-ug25UpqwR0 (expires Nov 23, 2024)
