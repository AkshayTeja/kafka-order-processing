from kafka import KafkaConsumer, KafkaProducer
import json

consumer = KafkaConsumer('orders', bootstrap_servers=['kafka:29092'], 
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

producer = KafkaProducer(bootstrap_servers=['kafka:29092'],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

for message in consumer:
    order = message.value
    
    # Data validation
    if order['quantity'] <= 0 or order['price'] <= 0:
        producer.send('invalid_orders', value=order)
        continue
    
    # Enrich order with total value
    order['total_value'] = order['quantity'] * order['price']
    
    # Send to enriched_orders topic
    producer.send('enriched_orders', value=order)

# create_connectors.sh
#!/bin/bash

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