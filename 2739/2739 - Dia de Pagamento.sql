SELECT name, CAST(EXTRACT(day FROM payday) AS INT)
FROM loan
