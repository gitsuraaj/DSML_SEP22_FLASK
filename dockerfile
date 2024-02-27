FROM python:3.9-slim-buster

WORKDIR /Users/suraaj/Desktop/docker

COPY requirements.txt /Users/suraaj/Desktop/docker/requirements.txt

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "--app", "hello", "run","--host=0.0.0.0"]
