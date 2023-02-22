FROM python:3.11

RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH "/root/.local/bin:$PATH"

WORKDIR /project
COPY pyproject.toml poetry.lock ./
RUN poetry install

WORKDIR /project/python
COPY python/ ./
CMD poetry run python main.py
