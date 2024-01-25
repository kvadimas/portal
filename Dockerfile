FROM python:3.11-alpine AS basic
WORKDIR /app
COPY /requirements.txt .
RUN pip3 install --upgrade pip && pip3 install -r /app/requirements.txt --no-cache-dir

FROM basic AS app
COPY portal .
CMD ["gunicorn", "portal.wsgi:application", "--bind", "0:8000" ]
