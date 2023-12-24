SELECT prd.name, prv.name, cat.name
FROM products prd
JOIN providers prv
	ON prd.id_providers = prv.id
	JOIN categories cat
	ON prd.id_categories = cat.id
WHERE prv.name LIKE 'Sansul SA' AND cat.name LIKE 'Imported'
