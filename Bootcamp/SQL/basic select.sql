use Northwind; -- This is the database

/* This is a sql query
It uses the customers table
*/

select * from dbo.Customers;

select companyname,city from dbo.Customers;

--Concatenation and Alias
select FirstName + ' ' + LastName as [Full Name]
from dbo.Employees;

select ProductName, 
	UnitPrice * (UnitsInStock + UnitsOnOrder) as SalesCalc
from dbo.Products;

