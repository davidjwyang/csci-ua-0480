-- 1) 
SELECT name 
FROM customers
WHERE flag = 't';

-- 2)
SELECT id
FROM inventory 
WHERE customer_email IS null;

-- 3) 
SELECT i.id, s.model_number, s.manufacturer, c.name, b.due 
FROM customer AS c 
INNER JOIN inventory AS i ON c.email = i.customer_email
INNER JOIN scooters AS s ON i.scooter_id = s.id
INNER JOIN borrows AS b i.id = b.item_id AND b.return_time is null
ORDER BY b.due;

-- 4) 
SELECT i.id, s.model_number, s.manufacturer, c.name
FROM customer AS c 
INNER JOIN inventory AS i ON c.email = i.customer_email
INNER JOIN scooters AS s ON i.scooter_id = s.id
INNER JOIN borrows AS b i.borrow_id = b.item_id;

-- 5)
SELECT refferal, COUNT(*) AS times_referred  
FROM customer 
GROUP BY referral 
ORDER BY COUNT(*) DESC
LIMIT 5;

-- 6) LET "EMAIL" be the unique identifier. 
SELECT id, item_id, checked_out
FROM borrows
WHERE customer_email = "EMAIL"
ORDER BY checked_out;

-- 7) LET "BORROW_ID" be the unique identifier. 
SELECT f.id, b.id, f.type, f.amount, 
FROM borrows as b 
INNER JOIN fees as f on b.id = f.borrow_id 
WHERE b.id = "BORROW_ID";

-- 8) 
SELECT * 
FROM manufacturers;


