FROM node:14

WORKDIR /app

RUN npm install -g json-server

COPY db.json .

CMD ["json-server", "--host", "0.0.0.0", "--port", "3000", "db.json"]