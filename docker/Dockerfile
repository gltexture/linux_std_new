FROM python:3.10.2-slim as builder
WORKDIR /app

COPY pyproject.toml .
COPY src/ ./src
COPY tests/ ./tests

RUN pip install --upgrade pip setuptools wheel && \
    pip install . pytest-asyncio && \
    pip install . httpx && \
    pip install . sqlalchemy
RUN pip install .


ENV PYTHONPATH=/app
FROM builder as test
ENV DATABASE_URL=postgresql://kubsu:kubsu@localhost:5432/kubsu
CMD ["pytest", "tests/", "--maxfail=1", "--disable-warnings", "-q", "--postgresql-host", "localhost"]


FROM python:3.10.2-slim
WORKDIR /app

COPY --from=builder /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app/src ./src

ENV PYTHONPATH=/app

EXPOSE 8086
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8086"]
