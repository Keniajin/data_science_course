SELECT COUNT(*) FROM (SELECT DISTINCT x.docid
FROM frequency x, frequency y
WHERE x.term = "transactions" AND y.term = "world" AND x.docid=y.docid);