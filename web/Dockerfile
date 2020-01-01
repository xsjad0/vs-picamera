FROM resin/raspberry-pi-python:3
ENTRYPOINT []

WORKDIR /home/web/
COPY . .

RUN pip3 install -r requirements.txt
RUN usermod -aG video root
RUN cd /home/web

EXPOSE 8080

CMD ["python3", "src/app.py"]
