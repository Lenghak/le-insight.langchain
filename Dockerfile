# 
FROM python:3.11 as requirements-stage

# 
WORKDIR /tmp

# 
RUN pip install poetry

# 
COPY ./pyproject.toml ./poetry.lock* /tmp/

# 
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# 
FROM python:3.11

# 
WORKDIR /app

# 
COPY --from=requirements-stage /tmp/requirements.txt /api/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

# 
COPY ./app /app
COPY .env .env

# 
CMD ["python3", "/app/main.py"]
