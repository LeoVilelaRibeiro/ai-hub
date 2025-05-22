FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
  build-essential \
  curl \
  && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml poetry.lock ./
COPY src ./src

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

EXPOSE 8501

CMD ["streamlit", "run", "src/ai-hub/streamlit_app.py", "--server.port=8501", "--server.enableCORS=false"]
