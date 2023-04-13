FROM python:latest

WORKDIR /kubernetes-censor-prototype

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "flask/app.py" ]