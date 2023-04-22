FROM python:latest

WORKDIR /kubernetes-censor-prototype

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_md

COPY . .

EXPOSE 8080
CMD [ "python", "flask/app.py" ]