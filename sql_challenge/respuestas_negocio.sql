-- 1. Clientes que cumplen años hoy con ventas > 1500 en enero 2020
SELECT c.first_name, c.last_name, c.email
FROM Customer c
JOIN Seller s ON c.email = s.customer_email
JOIN Item i ON s.seller_id = i.seller_id
JOIN PurchaseOrderItem poi ON i.item_id = poi.item_id
JOIN PurchaseOrder po ON poi.order_id = po.order_id
WHERE MONTH(c.birthdate) = MONTH(CURRENT_DATE) 
  AND DAY(c.birthdate) = DAY(CURRENT_DATE)
  AND MONTH(po.order_date) = 1 
  AND YEAR(po.order_date) = 2020
GROUP BY c.first_name, c.last_name, c.email
HAVING SUM(poi.quantity) > 1500;

-- 2. Top 5 vendedores por categoría y mes en 2020
SELECT 
  MONTH(po.order_date) AS month,  
  YEAR(po.order_date) AS year,
  c.first_name,
  c.last_name,  
  COUNT(*) AS sales,
  SUM(poi.quantity) AS products_sold,
  SUM(po.total_amount) AS total_amount
FROM PurchaseOrder po
INNER JOIN PurchaseOrderItem poi ON po.order_id = poi.order_id
INNER JOIN Item i ON poi.item_id = i.item_id
INNER JOIN Category cat ON i.category_id = cat.category_id
INNER JOIN Seller s ON i.seller_id = s.seller_id
INNER JOIN Customer c ON s.customer_email = c.email
WHERE YEAR(po.order_date) = 2020
  AND cat.name = 'Celulares' 
GROUP BY MONTH(po.order_date), YEAR(po.order_date), c.first_name, c.last_name
ORDER BY MONTH(po.order_date), SUM(po.total_amount) DESC
LIMIT 5;

-- 3. Registrar precio e estado actual en ItemPriceHistory

DELIMITER //
CREATE PROCEDURE insert_daily_price_history()
BEGIN
  INSERT INTO ItemPriceHistory (item_id, price, date)
    SELECT item_id, price, CURDATE()
    FROM ItemPrice;
END //
DELIMITER ;