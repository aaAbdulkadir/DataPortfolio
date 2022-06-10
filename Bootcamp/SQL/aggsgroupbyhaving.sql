use Northwind;

select * from dbo.Orders;

select sum(freight) as SumF,	
		count(Freight) as CountF,
		avg(coalesce(freight,0)) as AvgF,
		min(freight) as MinF,
		max(freight) as MaxF
from dbo.Orders;

select count(*) from dbo.Employees;

select count(Region) from dbo.Employees;

select * from dbo.Customers;

select  count(distinct country) from dbo.Customers;



select customerid,sum(freight) as SumF,	
		count(Freight) as CountF,
		avg(coalesce(freight,0)) as AvgF,
		min(freight) as MinF,
		max(freight) as MaxF
from dbo.Orders
group by CustomerID;


select customerid,sum(freight) as SumF,	
		count(Freight) as CountF,
		avg(coalesce(freight,0)) as AvgF,
		min(freight) as MinF,
		max(freight) as MaxF
from dbo.Orders
where sum(freight) > 1000 -- fails, cannot filter on a aggregate
group by CustomerID
 
;



select customerid,sum(freight) as SumF,	
		count(Freight) as CountF,
		avg(coalesce(freight,0)) as AvgF,
		min(freight) as MinF,
		max(freight) as MaxF
from dbo.Orders
where CustomerID like 'b%'
group by CustomerID
having sum(freight) > 1000 -- because it is filtering on an aggregate
;