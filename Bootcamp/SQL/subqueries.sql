use tsql;

--Self contained subqueries
select *
from sales.Orders
having freight > avg(freight);


select avg(freight) from sales.Orders;

select * from sales.Orders
where freight > 78.2442;

select * from sales.Orders
where freight > (select avg(freight) from sales.Orders);


-- Correlated Subqueries

select * from Production.Categories;
select * from Production.Products;

select count(*) from Production.Products
where categoryid = 3;

select C.categoryid,C.categoryname,
		(
			select count(P.productid) from Production.Products as P
				where P.categoryid = C.categoryid
		) as NumProds
from Production.Categories as C;

select C.categoryid,C.categoryname,count(P.productid) as NumProds
from Production.Categories as C left  join Production.Products as P
on P.categoryid = C.categoryid
group by C.categoryid,C.categoryname;

insert into Production.Categories (categoryname,description)
values ('Various','Other food')



select C.custid, C.companyname 
from sales.customers as C
where EXISTS
			(
				select * from sales.orders as O
				where o.custid = c.custid
			);


select C.custid, C.companyname 
from sales.customers as C
where (
				select count(*) from sales.orders as O
				where o.custid = c.custid
			) > 0;

select distinct C.custid, C.companyname 
from sales.customers as C inner join sales.orders as O
on o.custid = c.custid;


select C.custid, C.companyname 
from sales.customers as C
where NOT EXISTS
			(
				select * from sales.orders as O
				where o.custid = c.custid
			);

select  C.custid, C.companyname 
from sales.customers as C left join sales.orders as O
on o.custid = c.custid
where o.orderid is NULL;

select C.custid, C.companyname 
from sales.customers as C
where (
				select count(*) from sales.orders as O
				where o.custid = c.custid
			) = 0;