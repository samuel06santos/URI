SELECT doc.name, SUM(ROUND((att.hours * 150) * ( 1 + ws.bonus/100), 1)) salary
FROM attendances att
JOIN doctors doc ON att.id_doctor = doc.id
JOIN work_shifts ws ON att.id_work_shift = ws.id
GROUP BY doc.name
ORDER BY salary DESC