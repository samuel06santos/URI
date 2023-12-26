SELECT ctm.name, ren.rentals_date
FROM customers ctm
JOIN rentals ren
ON ctm.id = ren.id_customers
WHERE ren.rentals_date
	BETWEEN '2016-09-01' AND '2016-09-30'
