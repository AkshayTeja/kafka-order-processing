CREATE TABLE IF NOT EXISTS enriched_orders (
    order_id VARCHAR(255) PRIMARY KEY,
    product_name VARCHAR(255),
    quantity INT,
    price DECIMAL(10, 2),
    order_date TIMESTAMP,
    total_value DECIMAL(10, 2)
);