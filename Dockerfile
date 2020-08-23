FROM python:3.8

ENV \
    # Python
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \    
    # PIP
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # Poetry
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry'

# Install git
RUN apt-get update \
  && apt-get install -y git

WORKDIR /templates

COPY . ./

RUN pip install poetry==1.0.* \
  && poetry install

CMD poetry run cookiecutter -o /connector /templates
