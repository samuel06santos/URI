SELECT prd.name, prv.name, prd.price
FROM products prd
JOIN providers prv ON prv.id = prd.id_providers
JOIN categories cat ON cat.id = prd.id_categories
WHERE prd.price > 1000 AND cat.name = 'Super Luxury'
