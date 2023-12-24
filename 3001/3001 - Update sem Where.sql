SELECT prd.name,
	CASE WHEN prd.type = 'A' THEN 20.0 ELSE 
    CASE WHEN prd.type = 'B' THEN 70.0 ELSE 
    CASE WHEN prd.type = 'C' THEN 530.5 ELSE 0 END END END
    AS price
FROM products prd
ORDER BY prd.type, prd.id DESC
