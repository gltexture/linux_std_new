FROM python:3.10.2-slim as builder
WORKDIR /app

COPY pyproject.toml .
COPY src/ ./src
COPY tests/ ./tests

RUN pip install --upgrade pip setuptools wheel && \
    pip install . pytest-asyncio && \
    pip install . httpx && \
    pip install . sqlalchemy && \
    pip install . psycopg2
RUN pip install .


ENV PYTHONPATH=/app
ENV DATABASE_URL=postgresql://kubsu:kubsu@localhost:5432/kubsu
ENV POSTGRES_HOST=localhost
ENV POSTGRES_USER=kubsu
ENV POSTGRES_PASSWORD=kubsu
ENV POSTGRES_DB=kubsu
FROM builder as test
CMD ["pytest", "tests/", "--maxfail=1", "--disable-warnings", "-q"]


FROM python:3.10.2-slim
WORKDIR /app

COPY --from=builder /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app/src ./src

ENV PYTHONPATH=/app

EXPOSE 8086
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8086"]
