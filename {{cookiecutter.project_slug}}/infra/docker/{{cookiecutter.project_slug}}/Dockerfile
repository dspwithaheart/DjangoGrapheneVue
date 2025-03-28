FROM dockerRegistry/it/kanikoimagebuilder/python:3.13.0-slim  as install
# Dockerfile for Kaniko
#!! Kaniko runs Dockerfile from Project Root so paths are relative
#   to project root not from where Dockerfile ist located
COPY . /app

WORKDIR /app

RUN uv pip install . --system
WORKDIR /app/src/sciadataprepdjango

RUN mkdir -p $STATIC_ROOT
RUN mkdir -p $DIR_LOG

FROM install as setup

EXPOSE 8000

COPY infra/docker/sciadataprep/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
