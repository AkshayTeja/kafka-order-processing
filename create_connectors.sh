echo "Creating HTTP Source connector"
curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d '{
    "name": "http_source",
    "config": {
        "connector.class": "io.confluent.connect.http.HttpSourceConnector",
        "tasks.max": "1",
        "http.url": "http://json-server:3000/orders",
        "http.poll.interval.ms": "5000",
        "kafka.topic": "orders",
        "http.headers": "Content-Type:application/json",
        "key.converter": "org.apache.kafka.connect.storage.StringConverter",
        "value.converter": "org.apache.kafka.connect.json.JsonConverter",
        "value.converter.schemas.enable": "false"
    }
}'

echo "Creating PostgreSQL Sink connector"
curl -X POST http://localhost:8083/connectors -H "Content-Type: application/json" -d '{
    "name": "postgres_sink",
    "config": {
        "connector.class": "io.confluent.connect.jdbc.JdbcSinkConnector",
        "tasks.max": "1",
        "connection.url": "jdbc:postgresql://postgres:5432/orders_db",
        "connection.user": "user",
        "connection.password": "password",
        "auto.create": "true",
        "auto.evolve": "true",
        "delete.enabled": "false",
        "insert.mode": "upsert",
        "pk.mode": "record_key",
        "pk.fields": "order_id",
        "topics": "enriched_orders",
        "key.converter": "org.apache.kafka.connect.storage.StringConverter",
        "value.converter": "org.apache.kafka.connect.json.JsonConverter",
        "value.converter.schemas.enable": "false"
    }
}'