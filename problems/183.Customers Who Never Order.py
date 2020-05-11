# Write your MySQL query statement below

select Name as Customers from Customers
left join Orders
ON Customers.ID=Orders.CustomerId
where Orders.CustomerId IS NULL