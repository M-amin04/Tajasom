FROM python:3.12

ENV PYTHONDONTWRITTEBTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN mkdir -p /vol/web/static /vol/web/media


RUN apt-get update && apt-get install -y package_name && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install --no-cache-dir celery redis

COPY . .

RUN python manage.py collectstatic --noinput

RUN adduser --disabled-password --no-create-home django_user
RUN chown -R django_user:django_user /app /vol
USER django_user

CMD ["gunicorn", "my_project_name.wsgi:application", "--bind", "0.0.0.0:8000"]