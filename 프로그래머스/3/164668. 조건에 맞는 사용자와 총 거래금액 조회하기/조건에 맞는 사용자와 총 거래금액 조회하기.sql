-- 코드를 입력하세요
SELECT U.USER_ID, U.NICKNAME, SUM(B.PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD AS B
JOIN USED_GOODS_USER AS U
ON B.WRITER_ID = U.USER_ID
WHERE B.STATUS = 'DONE'
GROUP BY B.WRITER_ID
HAVING SUM(B.PRICE) >= 700000
ORDER BY SUM(B.PRICE)