SELECT
	lr.name,
    ROUND(lr.omega * 1.618, 3)
FROM life_registry lr
JOIN dimensions d
ON lr.dimensions_id = d.id
WHERE lr.name LIKE 'Richard%' AND d.name IN ('C875', 'C774')
ORDER BY lr.omega ASC
