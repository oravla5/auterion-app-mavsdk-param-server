# Libmav Telemetry Python

## Introduction

This is a simple Python script that leverages [libmav Python](https://github.com/Auterion/libmav-python/) to fetch telemetry from the Autopilot. The advantages of libmav are its simplicity and low-size while providing full interaction through raw [mavlink messages](https://mavlink.io/en/messages/common.html).

The directory `./services/telemetry` contains [mavlink dialect files](github.com/mavlink/mavlink/) in the XML format that are required by libmav. The folder structure of this example docker service is as follows:

```
services/telemetry/
├── Dockerfile
├── libmav_telemetry.py
└── mavlink
    ├── common.xml
    ├── minimal.xml
    └── standard.xml
```

It would just as well be possible to include mavlink directly as a git submodule.

This example is using an official Python Docker base image based on alpine ( currently `python:3.11.6-alpine3.18`) due to its incredibly low size of less than 20 MB, which results in equally small AuterionOS applications. If instead a Debain system is required for more flexibility, consider using the official "slim" Docker images from Python, such as `python:3.11-slim-bullseye`. These are two to three times larger than the Alpine images, but still an order of magnitude smaller than the regular full size images such as `python:3.12` for example.


## Commands

### Package and deploy

This is an application for AuterionOS. Build and install it with `auterion-cli`

**Build**

```shell
auterion-cli app build
```

It will create an app artifact in `build/libmav-telemetry-python.auterionos`.

After a successful build, you can connect your board via ethernet and run the following command to install the application on your device:

```shell
auterion-cli app install `build/libmav-telemetry-python.auterionos`
```


The application execution can be monitored by running the following command:

```shell
auterion-cli app logs libmav-telemetry-python -f
```

You can stop and remove the application with the following commands:

```shell
auterion-cli app remove libmav-telemetry-python
```