SELECT vt.amount AS most_frequent_value
FROM value_table vt
GROUP BY vt.amount
ORDER BY COUNT(*) DESC
LIMIT 1
