use Northwind;

select left(firstname, 1) + '. ' + lastname 
from dbo.Employees;

select right(firstname, 2) + '. ' + lastname 
from dbo.Employees;

select substring(firstname, 5,1) + '. ' + lastname 
from dbo.Employees;

select reverse(firstname) + '. ' + lastname 
from dbo.Employees;

select getdate();
select GETUTCDATE();

select orderid, datediff(dd,OrderDate,RequiredDate) 
from dbo.Orders;

select year(getdate())

select * from dbo.orders
where year(orderdate) = 1996 and month(orderdate) = 7;


select 1 + 'hello';

select cast(1 as varchar) + 'hello';

select convert(varchar,1) + 'hello';


select EmployeeID,city,Region,Country,
		city + ' ' + coalesce(Region,'') + ' ' + country as Place
from  dbo.Employees;

select EmployeeID,city,Region,Country,
		CONCAT(city, ' ',Region,' ',country) as Place
from  dbo.Employees;


select concat(1,'hello');



select getdate();

select convert(varchar,getdate());

select convert(varchar,getdate(),101);

select convert(varchar,getdate(),103);

select convert(varchar,getdate(),102);


select orderid, convert(varchar,OrderDate,103) as UKDate
from dbo.orders;