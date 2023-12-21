SELECT movies.id, movies.name
FROM movies join prices on movies.id_prices = prices.id
where prices.value < 2.00
