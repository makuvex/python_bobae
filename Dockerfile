FROM python:3.8
COPY . /app
WORKDIR /app

RUN pip install flask
RUN pip install flask-restful
RUN pip install flask-mysql
RUN pip3 install PyMysql

EXPOSE 5000
CMD ["python", "app.py"]
