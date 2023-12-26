SELECT
	cddt.name,
    ROUND( ((scr.math * 2) + (scr.specific * 3 ) + (project_plan * 5)) / 10 , 2) AS avg_score
FROM candidate cddt
JOIN score scr
ON cddt.id = scr.candidate_id
ORDER BY avg_score DESC
