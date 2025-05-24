FROM python:3.10.2-slim as builder

WORKDIR /app

COPY pyproject.toml .
COPY src/ ./src
COPY tests/ ./tests

RUN pip install --upgrade pip setuptools wheel && \
pip install -e . pytest-asyncio httpx sqlalchemy

FROM builder as test
ENV PYTHONPATH=/app
WORKDIR /app
CMD ["pytest", "tests/", "--maxfail=1", "--disable-warnings", "-q"]

FROM python:3.10.2-slim

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app/src ./src

ENV PYTHONPATH=/app

EXPOSE 8086
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8086"]
