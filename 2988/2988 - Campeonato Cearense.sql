SELECT
	tm.name as time,
    COUNT(mt.id) partidas,
    SUM(CASE WHEN (tm.id = mt.team_1 AND mt.team_1_goals > mt.team_2_goals) OR (tm.id = mt.team_2 AND mt.team_2_goals > mt.team_1_goals) THEN 1 ELSE 0 END) vitorias,
	SUM(CASE WHEN (tm.id = mt.team_1 AND mt.team_2_goals > mt.team_1_goals) OR (tm.id = mt.team_2 AND mt.team_1_goals > mt.team_2_goals) THEN 1 ELSE 0 END) derrotas,
	SUM(CASE WHEN mt.team_1_goals = mt.team_2_goals THEN 1 ELSE 0 END) empates,
    SUM(CASE
       		WHEN (tm.id = mt.team_1 AND mt.team_1_goals > mt.team_2_goals) OR (tm.id = mt.team_2 AND mt.team_2_goals > mt.team_1_goals) THEN 3
       		WHEN mt.team_1_goals = mt.team_2_goals THEN 1
       		ELSE 0 
       	END) pontos
FROM
	teams tm
LEFT JOIN
	matches mt ON tm.id = mt.team_1 OR tm.id = mt.team_2
GROUP BY
	tm.name
ORDER BY
	pontos DESC, vitorias DESC, empates DESC