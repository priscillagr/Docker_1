FROM python:3-onbuild
ADD . /todo
WORKDIR /todo
CMD ["python", "./app.py"]
