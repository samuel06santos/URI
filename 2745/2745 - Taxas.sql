SELECT
	people.name,
    ROUND(people.salary * 0.1, 2) as tax
FROM people
WHERE people.salary > 3000
