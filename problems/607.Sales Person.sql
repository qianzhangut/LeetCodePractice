# Write your MySQL query statement below
select name from SalesPerson s
where sales_id not in (select sales_id from Orders d join Company c on d.com_id=c.com_id where c.name = 'RED')