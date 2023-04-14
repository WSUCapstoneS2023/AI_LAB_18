FROM python:latest

WORKDIR /kubernetes-censor-prototype

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download en_core_web_md

COPY . .

EXPOSE 5000
CMD [ "python", "flask/app.py" ]
#CMD [ "python", "-m" , "flask.app", "run", "--host=0.0.0.0"]