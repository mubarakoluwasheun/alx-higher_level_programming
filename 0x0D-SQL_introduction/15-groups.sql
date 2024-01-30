-- Lists the number of records with the same score in the table second_table
-- Sorted by number of records (decending)
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
