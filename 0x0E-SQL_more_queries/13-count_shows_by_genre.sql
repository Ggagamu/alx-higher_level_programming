-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT p.'name' AS 'genre',
	COUNT(*) AS 'number_of_shows'
FROM 'tv_genres' AS p
	INNER JOIN 'tv_show_genres' AS o ON p.'id' = i.'genre_id'
GROUP BY p.'name'
ORDER BY 'number_of_shows' DESC;
