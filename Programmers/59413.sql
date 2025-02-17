
#MYSQL
SET @HOUR = -1;     # 변수생성하고 하나씩늘려서 사용
SELECT
    (@HOUR := @HOUR + 1) AS HOUR,
    (SELECT COUNT(ANIMAL_ID) AS COUNT FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @HOUR) AS COUNT
FROM
    ANIMAL_OUTS
WHERE
    @HOUR < 23          # @HOUR : -1 ~ 22, WHERE > SELECT이기 때문에 0시~23시 데이터가 select됨