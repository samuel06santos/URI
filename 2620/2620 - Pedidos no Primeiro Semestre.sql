SELECT cust.name, orders.id
FROM customers cust
JOIN orders ON cust.id = orders.id_customers
WHERE orders.orders_date BETWEEN
TO_DATE('01/01/2016', 'DD/MM/YYYY') AND TO_DATE('30/06/2016', 'DD/MM/YYYY')
