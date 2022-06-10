use Northwind;

select * from dbo.Customers
order by Country desc, city asc
;

select CompanyName, ContactName,city,Country from dbo.Customers
order by 3;   -- AVOID  - Really BAD Practice


select ProductName, 
	UnitPrice * (UnitsInStock + UnitsOnOrder) as SalesCalc
from dbo.Products
where UnitPrice * (UnitsInStock + UnitsOnOrder) > 200
order by SalesCalc;

select distinct country
from dbo.Customers;

select country
from dbo.Customers
group by country;

select distinct country, city
from dbo.Customers;


select top 10 percent * 
from dbo.Customers
order by CustomerID desc;


select top 20 with ties  * 
from dbo.Customers
order by CustomerID desc;


