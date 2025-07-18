-- 코드를 작성해주세요
SELECT I.ITEM_ID, I.ITEM_NAME, I.RARITY
FROM ITEM_INFO AS I
JOIN ITEM_TREE AS T ON I.ITEM_ID = T.ITEM_ID
JOIN ITEM_INFO AS P ON T.PARENT_ITEM_ID = P.ITEM_ID
WHERE P.RARITY = 'RARE'
ORDER BY I.ITEM_ID DESC