use northwind;
go
create view dbo.vNames
as
	select FirstName, lastname, city, Country
	from dbo.Employees;
go

select * from dbo.vNames;