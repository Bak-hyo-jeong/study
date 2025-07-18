-- 코드를 입력하세요
SELECT A.CATEGORY AS CATEGORY, SUM(B.SALES) AS TOTAL_SALES
FROM BOOK AS A
JOIN ( SELECT BOOK_ID, SUM(SALES) AS SALES
      FROM BOOK_SALES
      WHERE YEAR(SALES_DATE) = 2022 AND MONTH(SALES_DATE) = 1
      GROUP BY BOOK_ID
) AS B
ON A.BOOK_ID = B.BOOK_ID
GROUP BY CATEGORY
ORDER BY CATEGORY