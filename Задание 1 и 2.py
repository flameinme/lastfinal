Задание номер 1

SELECT c.login, COUNT(o.id)
FROM "Couriers" as c
INNER JOIN "Orders" as o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login;



Задание номер 2


SELECT track,
  CASE
  WHEN finished = true THEN 2
  WHEN cancelled = true THEN -1
  WHEN "Orders"."inDelivery" = true THEN 1
  ELSE 0
  END AS status
FROM "Orders";
