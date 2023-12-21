SELECT prd.name
FROM products prd
JOIN providers prv ON prv.id = prd.id_providers
WHERE (prd.amount BETWEEN 10 AND 20) AND (prv.name ILIKE 'P%')
