# pull official base image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# set work directory
WORKDIR /app


# copy requirements file
COPY ./requirements.txt /app/requirements.txt

# install dependencies
RUN pip install --upgrade pip setuptools wheel \
    && pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip
