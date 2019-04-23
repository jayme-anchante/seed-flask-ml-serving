FROM ubuntu:18.04

WORKDIR /home/

RUN apt update
RUN apt install --yes python3 python3-dev python3-pip
COPY requirements.txt ./
RUN pip3 install -r requirements.txt


ENV PYTHONPATH=$PYTHONPATH:/home/

# jupyter-lab
EXPOSE 8888
# flask
EXPOSE 9000

ENTRYPOINT ["python3", "app.py"]
