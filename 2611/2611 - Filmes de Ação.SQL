SELECT mv.id, mv.name FROM Movies mv
INNER JOIN Genres gr ON gr.id = mv.id_genres
WHERE gr.description = 'Action'
