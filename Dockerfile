# Dockerfile

# 베이스 이미지
FROM python:3.11-slim

# Docker 이미지 메타데이터
LABEL maintainer="minjoo.com"

# 파이썬 출력을 버퍼링 없이 즉시 보여주도록 설정
ENV PYTHONUNBUFFERED 1

# 의존성 설치를 위한 시스템 패키지 설치
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# uv 설치
RUN pip install uv

# 프로젝트 파일 복사
# 프로젝트 루트 디렉터리의 모든 파일을 컨테이너의 /app으로 복사합니다.
COPY . /app
WORKDIR /app
EXPOSE 8000

# 개발 환경인지 판단하는 변수
ARG DEV=false

# 필수 패키지 설치
RUN uv pip install -r /app/requirements.txt --system && \
    if [ "$DEV" = "true" ] ; then \
        uv pip install -r /app/requirements.dev.txt --system ; \
    fi

# 임시 파일 삭제
RUN rm -rf /tmp

# 일반 사용자 생성 및 권한 설정
RUN adduser --disabled-password --no-create-home django-user
RUN chown -R django-user:django-user /app

# Path 설정 및 사용자 전환
ENV PATH="/py/bin:$PATH"
USER django-user