use Northwind;

create table dbo.Workers
(
	wID		int			NOT NULL primary key identity(1,1),
	fname	varchar(30)	NOT NULL,
	Info	varchar(200) NULL
);


insert into dbo.workers(fname,info) values('Bert','Total idiot');

select * from dbo.workers;

insert into dbo.Workers(fname,Info)
	values('Doris','Really old'),
			('Ethel','Even older'),
			('Albert','Very ancient');

insert into dbo.Workers(fname)
	select FirstName
	from dbo.Employees;


update dbo.Workers
	set info = 'Nothing to say'
	where info is NULL;

select * from dbo.Workers;

update dbo.Workers
	set fname = 'Freddy',info = 'Nice person'
where wID = 1;


delete dbo.Workers
 where wID = 5;

select * from dbo.Workers;

insert into dbo.Workers(fname,info)
values('Sid','Bit Vicious');



begin tran

	truncate table dbo.Workers;

	select * from dbo.Workers

	insert into Workers(fname,Info) values ('Johnny','Bit Rotten');

	select *  from dbo.workers;

--commit tran
rollback tran



	select *  from dbo.workers;


	set identity_insert dbo.workers on;

	insert into dbo.Workers(wid,fname,info)
	values(5,'Jack','The Ripper');

	set identity_insert dbo.workers off;
