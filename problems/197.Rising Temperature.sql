# Write your MySQL query statement below
SELECT wt1.id FROM Weather wt1, Weather wt2
WHERE wt1.Temperature > wt2.Temperature AND 
      DATEDIFF(wt1.recordDate, wt2.recordDate)=1;