-- wrinting a scrip that list the numbers of records with same score
SELECT score, COUNT(*) number
FROM second_table 
GROUP BY score
ORDER BY score DESC