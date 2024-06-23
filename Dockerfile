FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /django

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /django/


#COPY . .
#
#EXPOSE 8001
#
#CMD ["python3", "manage.py", "runserver"]