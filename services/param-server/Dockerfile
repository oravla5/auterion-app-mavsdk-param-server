FROM auterion/app-base:v2
## FROM python:3.11.6-alpine3.18

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-grpcio
RUN pip install libmav
RUN pip install mavsdk

WORKDIR /app
COPY mavsdk_param_server.py mavsdk_param_server.py
COPY mavlink mavlink

CMD python3 mavsdk_param_server.py
