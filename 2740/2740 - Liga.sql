(SELECT 'Podium: ' || league.team AS name
 FROM league ORDER BY league.position ASC
 LIMIT 3
)

UNION ALL

(SELECT 'Demoted: ' || team FROM
 	(SELECT team, position FROM league
      ORDER BY position DESC
      LIMIT 2
     ) AS subquery
ORDER BY position ASC);
