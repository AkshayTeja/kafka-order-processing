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
