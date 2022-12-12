FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH="/"
WORKDIR /app_python
RUN ["mkdir", "/storage"]
RUN ["touch", "/storage/visits.json"]
RUN ["chown", "app_python", "/storage/visits.json"]
COPY requirements.txt /app_python/
RUN pip install -r requirements.txt
COPY . /app_python/
ENTRYPOINT python3 ./moscowtime/manage.py runserver
