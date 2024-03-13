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
WORKDIR /api

# 
COPY --from=requirements-stage /tmp/requirements.txt /api/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

# 
COPY ./src /api/src

# 
CMD ["python3", "/api/src/main.py"]
