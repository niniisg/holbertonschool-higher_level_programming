-- wrinting a scrip that list all records of table second_table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;