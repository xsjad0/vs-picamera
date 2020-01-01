FROM resin/raspberry-pi-python:3
ENTRYPOINT []

WORKDIR /home/mqtt/
COPY . .

RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install -y mosquitto
RUN usermod -aG video root
RUN cd /home/mqtt

EXPOSE 1883

CMD ["mosquitto"]
