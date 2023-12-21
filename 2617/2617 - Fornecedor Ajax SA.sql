SELECT prd.name, prov.name
FROM products prd JOIN providers prov
ON prov.id = prd.id_providers
WHERE prov.name = 'Ajax SA'
