FROM python:3.10.2-slim as builder

WORKDIR /app

COPY pyproject.toml setup.py .
COPY src/ ./src
COPY tests/ ./tests

RUN pip install --upgrade pip setuptools wheel && \
    pip install -e . && \
    pip install pytest-asyncio httpx sqlalchemy pytest

FROM builder as test
WORKDIR /app
ENV PYTHONPATH=/app
CMD ["pytest", "tests/"]

FROM python:3.10.2-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /app/src ./src
ENV PYTHONPATH=/app
EXPOSE 8086
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8086"]
