use Northwind;

select * from dbo.Customers
where city = 'london'  OR city = 'Paris' OR city = 'Berlin';


select * from dbo.Customers
where city not in ('london','Paris','Berlin');

select * from dbo.Orders
where OrderDate >= '19960701' AND orderdate <='19960731';

select * from dbo.Orders
where OrderDate between '19960701' AND '19960731';


select * from dbo.products
where (CategoryID = 7 OR CategoryID = 8)
AND UnitPrice > 30
;

select EmployeeID,city,Region,Country
from  dbo.Employees
where region is NULL;

select EmployeeID,city,Region,Country
from  dbo.Employees
where region is not NULL;

select EmployeeID,city,Region,Country,
		city + ' ' + isnull(Region,'') + ' ' + country as Place
from  dbo.Employees;

select EmployeeID,city,Region,Country,
		city + ' ' + coalesce(Region,'') + ' ' + country as Place
from  dbo.Employees;


select * from dbo.Customers
where city like 'L%';  -- % = 0 or more characters

select * from dbo.Customers
where city like '%L%';

select * from dbo.Customers
where city like 'L_'; --  _ = exactly 1 char

select * from dbo.Customers
where city like 'L___'; --  _ _ _ = exactly 3 char

select * from dbo.Customers
where city like 'L_%'; -- 1 or more characters


select * from dbo.Customers
where city like 'L[a-eoy]%';  -- [] any single character in that range

select * from dbo.Customers
where city like 'L[^aeiou]%';  --[^] any single char NOT in that range




