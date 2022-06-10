use Northwind;

--inner join - Customers with Orders
select C.companyname,O.OrderDate
from dbo.Customers as C inner join  dbo.Orders as O
on C.CustomerID = O.CustomerID;

--Left outer - all customers whether or not they have orders
select C.companyname,O.OrderDate
from dbo.Customers as C left outer join  dbo.Orders as O
on C.CustomerID = O.CustomerID;

--right outer - all orders whether or not they have customers
select C.companyname,O.OrderDate
from dbo.Customers as C right outer join  dbo.Orders as O
on C.CustomerID = O.CustomerID;

--full outer - all orders and customers
select C.companyname,O.OrderDate
from dbo.Customers as C full outer join  dbo.Orders as O
on C.CustomerID = O.CustomerID;

--Cross join
select C.companyname,O.OrderDate
from dbo.Customers as C cross join  dbo.Orders as O
;

select C.companyname,O.OrderDate,
		OD.Quantity,OD.UnitPrice,
		P.ProductName
from dbo.Customers as C left join  dbo.Orders as O
on C.CustomerID = O.CustomerID
						left join dbo.[Order Details] as OD
ON O.OrderID = OD.OrderID
						left join dbo.Products as P
on P.ProductID = OD.ProductID
;

select C.CompanyName as Customer,S.CompanyName as Supplier,
		C.city, c.Country
from dbo.Customers as C inner join dbo.Suppliers as S
on C.city = S.city AND C.Country = S.Country;


select E.FirstName as Employee, M.FirstName as Manager
from dbo.Employees as E left join dbo.Employees as M
on E.ReportsTo = M.EmployeeID;

