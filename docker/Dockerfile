FROM python:3.10.2-slim as builder
WORKDIR /app

COPY pyproject.toml .
COPY src/ ./src
COPY tests/ ./tests

RUN pip install --upgrade pip setuptools wheel && \
    pip install . pytest-asyncio httpx sqlalchemy asyncpg pytest

ENV PYTHONPATH=/app
FROM builder as test
EXPOSE 8086
CMD bash -c "uvicorn src.main:app --host 0.0.0.0 --port 8086 & sleep 3 && pytest -v tests/"

FROM python:3.10.2-slim
WORKDIR /app

COPY --from=builder /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app/src ./src

ENV PYTHONPATH=/app

EXPOSE 8086
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8086"]
