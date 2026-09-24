
FROM python:3.12-slim

WORKDIR /app

COPY processor.py .

RUN useradd --create-home appuser

RUN mkdir -p /data && chown appuser:appuser /data

USER appuser

VOLUME ["/data"]

CMD ["python", "processor.py"]