FROM --platform=linux/amd64 ghcr.io/astral-sh/uv:0.4.24-python3.13-bookworm

WORKDIR /workspace

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_LINK_MODE=copy

ENV UV_PROJECT_ENVIRONMENT="/usr/local/"

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project

COPY . /workspace
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

ENTRYPOINT []
