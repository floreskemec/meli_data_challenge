from faker import Faker
import random

fake = Faker()

# Generate data for Category
for i in range(1, 11):
    print(f"INSERT INTO Category (category_id, name, url) VALUES ({i}, '{fake.word()}', '{fake.url()}');")

# Generate data for Customer
emails = []
for i in range(1, 11):
    email = fake.email()
    emails.append(email)
    print(f"INSERT INTO Customer (email, first_name, last_name, gender, address, birthdate, phone) VALUES ('{email}', '{fake.first_name()}', '{fake.last_name()}', '{random.choice(['M', 'F'])}', '{fake.address().replace(',', ' ')}', '{fake.date_of_birth(minimum_age=18, maximum_age=90)}', '{fake.phone_number()}');")

# Generate data for Seller and Buyer
for i in range(1, 11):
    print(f"INSERT INTO Seller (seller_id, customer_email) VALUES ({i}, '{emails[i-1]}');")
    print(f"INSERT INTO Buyer (buyer_id, customer_email) VALUES ({i}, '{emails[i-1]}');")

# Generate data for Item
for i in range(1, 11):
    print(f"INSERT INTO Item (item_id, category_id, seller_id) VALUES ({i}, {random.randint(1, 10)}, {random.randint(1, 10)});")

# Generate data for ItemPrice and ItemPriceHistory
for i in range(1, 11):
    price = round(random.uniform(10.0, 500.0), 2)
    print(f"INSERT INTO ItemPrice (price_id, item_id, price, effective_date) VALUES ({i}, {i}, {price}, '{fake.date_this_year()}');")
    print(f"INSERT INTO ItemPriceHistory (history_id, item_id, price, date) VALUES ({i}, {i}, {price}, '{fake.date_this_year()}');")

# Generate data for PurchaseOrder
for i in range(1, 11):
    print(f"INSERT INTO PurchaseOrder (order_id, buyer_id, order_date, total_amount) VALUES ({i}, {random.randint(1, 10)}, '{fake.date_this_year()}', {round(random.uniform(10.0, 500.0), 2)});")

# Generate data for PurchaseOrderItem
for i in range(1, 11):
    print(f"INSERT INTO PurchaseOrderItem (order_item_id, order_id, item_id, quantity) VALUES ({i}, {random.randint(1, 10)}, {random.randint(1, 10)}, {random.randint(1, 5)});")