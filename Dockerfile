FROM python:3.12
ADD main.py ./main.py
EXPOSE 8080:8080
ENTRYPOINT python ./main.py