FROM python:3-slim
WORKDIR /home
RUN apt update && apt install -y python3-pip
RUN pip3 install google-cloud-storage
COPY habackup .
ENTRYPOINT ["python3","./main.py"]