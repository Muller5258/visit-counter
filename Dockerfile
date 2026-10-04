# ---- stage 1: build ----
FROM python:3.12-slim AS builder
WORKDIR /app
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- stage 2: run ----
FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"
COPY . .
RUN useradd -m appuser
USER appuser
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
