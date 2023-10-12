# 


FROM alpine:latest

# 


WORKDIR /code

RUN  apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN  apk add py3-pip

# 


COPY ./requirements.txt /code/requirements.txt

# 


RUN pip install -r /code/requirements.txt

# 


COPY ./ /code/flaskhello

# 


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
