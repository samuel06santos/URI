SELECT
	pkg.year AS year,
    u_sender.name AS sender,
    u_receiver.name AS receiver
    
FROM packages pkg
JOIN 
    users u_sender ON
    pkg.id_user_sender = u_sender.id
JOIN 
    users u_receiver ON
    pkg.id_user_receiver = u_receiver.id
    
WHERE 
    (pkg.color = 'blue' OR pkg.year = 2015)
    AND u_sender.address != 'Taiwan'
    AND u_receiver.address != 'Taiwan'
ORDER BY 
    pkg.year DESC;
