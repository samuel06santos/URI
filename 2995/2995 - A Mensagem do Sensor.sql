SELECT
	temperature,
    COUNT(temperature) AS number_of_records
from records
GROUP BY mark, temperature
ORDER BY mark
