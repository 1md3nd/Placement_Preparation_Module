# Write your MySQL query statement below
SELECT sell_date, count(distinct(product)) as num_sold,
GROUP_CONCAT(DISTINCT product ORDER BY product ASC SEPARATOR ',') AS products 
FROM activities
GROUP BY sell_date
ORDER BY sell_date ASC;
