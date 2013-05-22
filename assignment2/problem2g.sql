SELECT x.myvalue FROM (SELECT A.row_num as myrow, B.col_num as mycol, SUM(A.value*B.value) as myvalue
FROM A, B
WHERE A.col_num = B.row_num
GROUP BY A.row_num, B.col_num) as x
WHERE x.myrow=2 AND x.mycol = 3;