use Northwind;

select CompanyName, city, Phone from dbo.Customers
union
select CompanyName, City, phone from dbo.Suppliers
union
select LastName, City, HomePhone from dbo.Employees;

select CompanyName as Entity, city, Phone from dbo.Customers
union all
select CompanyName, City, phone from dbo.Suppliers
union all
select LastName, City, HomePhone from dbo.Employees;


select city from dbo.Customers
intersect
select city from dbo.Suppliers;


select city from dbo.Customers
except
select city from dbo.Suppliers;

select distinct C.city
from dbo.Customers as C left join dbo.Suppliers as S
on C.city = S.city
where S.city is NULL;