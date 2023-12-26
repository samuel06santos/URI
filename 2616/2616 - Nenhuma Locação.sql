SELECT ctm.id, ctm.name
FROM locations loc
FULL OUTER JOIN customers ctm
ON ctm.id = loc.id_customers
WHERE ctm.id IS NULL OR loc.id_customers IS NULL
ORDER BY ctm.id
