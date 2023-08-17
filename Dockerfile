FROM python:3.9-alpine

WORKDIR /usr/src/app/

ENV PYTHONUNBUFFERED 1
ENV DONTWRITEBYTECODE 1

COPY ./requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

RUN chmod +x /usr/src/app/start.sh

ENTRYPOINT [ "/usr/src/app/start.sh" ]
