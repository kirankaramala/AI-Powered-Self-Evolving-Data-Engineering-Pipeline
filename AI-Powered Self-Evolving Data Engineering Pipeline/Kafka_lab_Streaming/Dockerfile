FROM python:3.11-slim

RUN pip install \
    jupyterlab \
    kafka-python \
    requests
RUN pip install mysql-connector-python

COPY Bootstrap.py /bootstrap.py
COPY notebooks /notebooks

WORKDIR /notebooks

EXPOSE 8888

CMD ["python", "/bootstrap.py"]