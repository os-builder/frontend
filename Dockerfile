FROM python:alpine

RUN apk add npm

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./package.json /app/package.json

RUN npm install

COPY ./ /app

run npm run build

EXPOSE 7000

CMD ["python", "manage.py", "runserver"]
