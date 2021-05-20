FROM python:3-slim
WORKDIR /home
#RUN apk add --update py-pip
RUN apt update && apt install -y python3-pip
#COPY requirements.txt .
#RUN pip install -qr requirements.txt
RUN pip3 install google-cloud-storage
COPY habackup .
#CMD ["./main.py"]