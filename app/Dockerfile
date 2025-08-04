FROM python:3.12.2

WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip &&  python -m pip install -r requirements.txt

EXPOSE 5000

COPY . /app

# CMD [ "flask", "--app main", "create_db" ]