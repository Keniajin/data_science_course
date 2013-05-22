SELECT SUM(crude_view.count*earn_view.count)
FROM (SELECT * FROM frequency WHERE docid = "10080_txt_crude") as crude_view, 
(SELECT * FROM frequency WHERE docid = "17035_txt_earn") as earn_view
WHERE crude_view.term = earn_view.term;