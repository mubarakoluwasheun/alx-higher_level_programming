-- Lists all records of the table second_table of the database
-- Records should be listed in descending score
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
