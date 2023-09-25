# 


FROM python:3.10

# 


WORKDIR /code

# 


COPY ./requirements.txt /code/requirements.txt

# 


RUN pip install /code/requirements.txt

# 


COPY ./flashello /code/flashello

# 


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
