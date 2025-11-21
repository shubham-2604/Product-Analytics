import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

# Configuration
n_orders = 1000

# Product catalog
products = {
    'Electronics': [
        ('P001', 'Laptop', 899.99),
        ('P002', 'Smartphone', 699.99),
        ('P003', 'Tablet', 399.99),
        ('P004', 'Headphones', 149.99),
        ('P005', 'Monitor', 299.99)
    ],
    'Clothing': [
        ('P010', 'T-Shirt', 19.99),
        ('P011', 'Jeans', 49.99),
        ('P012', 'Jacket', 89.99),
        ('P013', 'Shoes', 79.99),
        ('P014', 'Sweater', 39.99)
    ],
    'Home': [
        ('P020', 'Coffee Maker', 79.99),
        ('P021', 'Blender', 59.99),
        ('P022', 'Lamp', 34.99),
        ('P023', 'Chair', 149.99),
        ('P024', 'Desk', 299.99)
    ],
    'Books': [
        ('P030', 'Novel', 14.99),
        ('P031', 'Cookbook', 24.99),
        ('P032', 'Textbook', 89.99),
        ('P033', 'Magazine', 9.99),
        ('P034', 'Comic Book', 12.99)
    ],
    'Sports': [
        ('P040', 'Yoga Mat', 29.99),
        ('P041', 'Dumbbells', 49.99),
        ('P042', 'Running Shoes', 99.99),
        ('P043', 'Tennis Racket', 79.99),
        ('P044', 'Basketball', 24.99)
    ]
}

# Generate orders
orders = []
for order_id in range(1001, 1001 + n_orders):
    # Random category and product
    category = np.random.choice(list(products.keys()))
    product_list = products[category]
    product = product_list[np.random.randint(0, len(product_list))]
    product_id, product_name, price = product
    
    # Random attributes
    quantity = np.random.randint(1, 5)
    order_date = (datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 365))).strftime('%Y-%m-%d')
    customer_id = f"C{np.random.randint(100, 999)}"
    region = np.random.choice(['North', 'South', 'East', 'West'])
    
    orders.append({
        'order_id': order_id,
        'product_id': product_id,
        'product_name': product_name,
        'category': category,
        'quantity': quantity,
        'price': price,
        'order_date': order_date,
        'customer_id': customer_id,
        'region': region
    })

# Create DataFrame
df = pd.DataFrame(orders)

# Save
df.to_csv('./sample_sales.csv', index=False)
print(f"✅ Generated {len(df)} sales records")
print(f"\nCategories: {df['category'].value_counts().to_dict()}")
print(f"Date range: {df['order_date'].min()} to {df['order_date'].max()}")
print(f"Total revenue: ${(df['quantity'] * df['price']).sum():,.2f}")