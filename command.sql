﻿# Задание 1
SELECT COUNT(o."inDelivery") , c.login
FROM "Orders" AS o
INNER JOIN "Couriers" AS c ON o."courierId"=c.id
WHERE o.“inDelivery” = true
GROUP BY c.login;

# Задание 2
SELECT track,
CASE WHEN finished = true THEN ‘2’
     WHEN canсelled = true THEN ‘-1’
     WHEN “inDelivery” = true THEN ‘1’
     ELSE ‘0’ END
FROM “Orders” ;
