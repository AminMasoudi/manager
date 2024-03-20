FROM python:3.10-slim-bullseye

RUN apt-get update

RUN apt-get install -y --no-install-recommends --no-install-suggests \
  build-essential \
  && pip install --no-cache-dir --upgrade pip

WORKDIR /opt/app

COPY requirements.txt .

RUN pip install --no-cache-dir --requirement requirements.txt

COPY manage.py .
COPY task_manager/ .
COPY core/ .
COPY task/ .
COPY . .

EXPOSE 8000
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py init_task_app

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
