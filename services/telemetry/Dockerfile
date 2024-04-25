FROM python:3.11.6-alpine3.18

RUN pip install libmav

WORKDIR /app
COPY libmav_telemetry.py libmav_telemetry.py
COPY mavlink mavlink

CMD python3 libmav_telemetry.py
