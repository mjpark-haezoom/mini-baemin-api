# 베이스 이미지
FROM python:3.11-slim
LABEL maintainer="minjoo.com"
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

RUN pip install uv

# 프로젝트 복사
COPY . /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN uv pip install -r /app/requirements.txt --system && \
    if [ "$DEV" = "true" ] ; then \
        uv pip install -r /app/requirements.dev.txt --system ; \
    fi

# /tmp 권한 보장 (sticky bit)
RUN mkdir -p /tmp && chmod 1777 /tmp

# 일반 사용자 생성 및 권한 설정
RUN adduser --disabled-password --no-create-home django-user
RUN chown -R django-user:django-user /app

# Ruff 캐시 경로 고정
ENV RUFF_CACHE_DIR=/tmp/ruff_cache

ENV PATH="/py/bin:$PATH"
USER django-user
