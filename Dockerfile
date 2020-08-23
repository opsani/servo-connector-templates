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

WORKDIR /templates

# Install dependencies first to get cache hits
COPY pyproject.toml poetry.lock ./
RUN pip install poetry==1.0.* \
  && poetry install

COPY . ./

ENTRYPOINT ["poetry", "run", "cookiecutter", "-o", "/build", "/templates"]
CMD ["--help"]
