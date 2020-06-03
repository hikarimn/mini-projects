FROM python:3.7-alpine
WORKDIR /app
ADD requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app
ENTRYPOINT ["python"]
CMD ["app.py"]
