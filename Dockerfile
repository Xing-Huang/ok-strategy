FROM ubuntu:18.04

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y python3
RUN apt-get install -y python3-pip

WORKDIR .
RUN mkdir app
COPY . /app/
RUN pip3 install  -i https://pypi.tuna.tsinghua.edu.cn/simple -r /app/requirements.txt

CMD ["python3", "/app/app.py"]
