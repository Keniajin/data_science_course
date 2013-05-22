SELECT SUM(f.count) as total
FROM frequency f
WHERE f.term IN ("washington", "taxes", "treasury")
GROUP BY f.docid
ORDER BY total DESC
LIMIT 1;