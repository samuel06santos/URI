SELECT prd.name, cat.name
FROM products prd
JOIN categories cat
ON prd.id_categories = cat.id
WHERE prd.amount > 100
AND cat.id IN (1, 2, 3, 6, 9)
ORDER BY cat.id
