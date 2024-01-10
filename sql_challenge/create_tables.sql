CREATE TABLE Category (
  category_id INT PRIMARY KEY,
  name VARCHAR(255),
  url VARCHAR(255)
);

CREATE TABLE Customer (
  email VARCHAR(255) PRIMARY KEY,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  gender CHAR(1),
  address VARCHAR(255), 
  birthdate DATE,
  phone VARCHAR(20)
); 

CREATE TABLE Seller (
  seller_id INT PRIMARY KEY,
  customer_email VARCHAR(255),
  FOREIGN KEY (customer_email) REFERENCES Customer(email)
);

CREATE TABLE Buyer (
  buyer_id INT PRIMARY KEY,
  customer_email VARCHAR(255),
  FOREIGN KEY (customer_email) REFERENCES Customer(email)
);

CREATE TABLE Item (
  item_id INT PRIMARY KEY,
  category_id INT,
  seller_id INT,
  FOREIGN KEY (category_id) REFERENCES Category(category_id),
  FOREIGN KEY (seller_id) REFERENCES Seller(seller_id)
);

CREATE TABLE ItemPrice (
  price_id INT PRIMARY KEY, 
  item_id INT,
  price DECIMAL(10,2),
  effective_date DATE,
  FOREIGN KEY (item_id) REFERENCES Item(item_id)
);

CREATE TABLE ItemPriceHistory (
  history_id INT PRIMARY KEY,
  item_id INT,
  price DECIMAL(10,2),
  date DATE,
  FOREIGN KEY (item_id) REFERENCES Item(item_id)
);

CREATE TABLE PurchaseOrder (
  order_id INT PRIMARY KEY,
  buyer_id INT,
  order_date DATE,
  total_amount DECIMAL(10,2),
  FOREIGN KEY (buyer_id) REFERENCES Buyer(buyer_id)
);

CREATE TABLE PurchaseOrderItem (
  order_item_id INT PRIMARY KEY,
  order_id INT,
  item_id INT,
  quantity INT,
  FOREIGN KEY (order_id) REFERENCES PurchaseOrder(order_id),
  FOREIGN KEY (item_id) REFERENCES Item(item_id)
);