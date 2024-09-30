# Dockerfile
FROM node:14

WORKDIR /app

RUN npm install -g json-server

COPY db.json .

# Add a health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:3000/orders || exit 1

CMD ["json-server", "--host", "0.0.0.0", "--port", "3000", "db.json"]