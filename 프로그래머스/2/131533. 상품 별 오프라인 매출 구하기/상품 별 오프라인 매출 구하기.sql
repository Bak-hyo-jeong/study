-- 코드를 입력하세요
SELECT P.PRODUCT_CODE, P.PRICE * SUM(O.SALES_AMOUNT) AS SALES
FROM PRODUCT AS P
INNER JOIN OFFLINE_SALE AS O
ON P.PRODUCT_ID = O.PRODUCT_ID
GROUP BY P.PRODUCT_CODE
ORDER BY SALES DESC, P.PRODUCT_CODE ASC