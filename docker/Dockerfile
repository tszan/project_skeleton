FROM python:3.9

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV PYTHONUNBUFFERED 1
ENV PYTHONFAULTHANDLER 1

# Native Dependencies
RUN apt-get update && \
    apt-get install --quiet --yes --no-install-recommends \
        && true && \
    rm -rf /var/log/apt* \
    rm -rf /var/log/dpkg* \
    rm -rf /var/lib/apt/lists/*

# Put Project Sources
COPY . ./app
WORKDIR /app

# Install PIP Dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --default-timeout=600 -r ./app/pip-requirements.txt

EXPOSE 5000