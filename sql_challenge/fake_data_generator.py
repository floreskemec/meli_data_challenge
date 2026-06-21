import faker
import random
import datetime

fake = faker.Faker()

# Set desired number of datapoints
num_datapoints = 100

# Name of the output SQL file
output_file = 'insert_data.sql'

# Create or open the SQL file in write mode
with open(output_file, 'w') as sql_file:
    # Generate and insert data into the Category table
    for category_id in range(1, num_datapoints + 1):
        name = fake.word()
        url = 'url_' + name.lower()
        sql_file.write(f"INSERT INTO Category (category_id, name, url) VALUES ({category_id}, '{name}', '{url}');\n")

    # Generate and insert data into the Customer table
    emails = [fake.email() for _ in range(num_datapoints)]
    for email_id, email in enumerate(emails, start=1):
        first_name = fake.first_name()
        last_name = fake.last_name()
        gender = random.choice(['M', 'F'])
        address = fake.address().replace('\n', ', ')
        birthdate = fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%Y-%m-%d')
        phone = fake.phone_number()
        sql_file.write(f"INSERT INTO Customer (email, first_name, last_name, gender, address, birthdate, phone) VALUES ('{email}', '{first_name}', '{last_name}', '{gender}', '{address}', '{birthdate}', '{phone}');\n")

        # Generate and insert data into the Seller and Buyer tables
        sql_file.write(f"INSERT INTO Seller (seller_id, customer_email) VALUES ({email_id}, '{email}');\n")
        sql_file.write(f"INSERT INTO Buyer (buyer_id, customer_email) VALUES ({email_id}, '{email}');\n")

    # Generate and insert data into the Item table
    for item_id in range(1, num_datapoints + 1):
        category_id = random.randint(1, num_datapoints)
        seller_id = random.randint(1, num_datapoints)
        sql_file.write(f"INSERT INTO Item (item_id, category_id, seller_id) VALUES ({item_id}, {category_id}, {seller_id});\n")

    # Generate and insert data into the ItemPrice and ItemPriceHistory tables
    for price_id in range(1, num_datapoints + 1):
        item_id = random.randint(1, num_datapoints)
        price = round(random.uniform(10.0, 500.0), 2)
        effective_date = fake.date_this_decade().strftime('%Y-%m-%d')
        sql_file.write(f"INSERT INTO ItemPrice (price_id, item_id, price, effective_date) VALUES ({price_id}, {item_id}, {price}, '{effective_date}');\n")
        sql_file.write(f"INSERT INTO ItemPriceHistory (history_id, item_id, price, date) VALUES ({price_id}, {item_id}, {price}, '{effective_date}');\n")

    # Generate and insert data into the PurchaseOrder and PurchaseOrderItem tables
    for order_id in range(1, num_datapoints + 1):
        buyer_id = random.randint(1, num_datapoints)
        order_date = fake.date_this_year().strftime('%Y-%m-%d')
        total_amount = round(random.uniform(10.0, 500.0), 2)
        sql_file.write(f"INSERT INTO PurchaseOrder (order_id, buyer_id, order_date, total_amount) VALUES ({order_id}, {buyer_id}, '{order_date}', {total_amount});\n")

        # Ensure the item_id exists in the Item table
        item_id = random.randint(1, num_datapoints)
        quantity = random.randint(1, 5)
        sql_file.write(f"INSERT INTO PurchaseOrderItem (order_item_id, order_id, item_id, quantity) VALUES ({order_id}, {order_id}, {item_id}, {quantity});\n")