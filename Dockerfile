FROM python:3.12-slim

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

COPY . /app/

EXPOSE 8000

# Run the application
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
