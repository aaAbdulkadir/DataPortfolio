use northwind;
go

alter proc dbo.uspNames
	@c	varchar(20)
as
begin
	select FirstName + ' ' + lastname as Fullname
	from dbo.Employees
	where city = @c;
end;

go

exec dbo.uspnames  @c='London';