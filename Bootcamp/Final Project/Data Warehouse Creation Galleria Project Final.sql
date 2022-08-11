/***

CREATE A STAR SCHEMA BASED ON THE PLAN CREATED:

Fact Table: 
- [SaleID, SaleDate, TicketNo, Stock_Code, OutletID, CardID, ProductGroup, OrderQty, Total] --> SalesID is primary key

Dimension Tables: 
-    - [Product_Group, Group_name]
    - [StockCode, Name, Description, Price]
    - [OutletID, Outlet]
    - [CardID, CardType]

***/

CREATE DATABASE Galleria

USE Galleria
GO

---------- DROP TABLE TO ENSURE CREATION IF EXISTS ----------
BEGIN
	DROP TABLE dbo.SalesFact
	DROP TABLE dbo.GroupDimension
	DROP TABLE dbo.NameDimension
	DROP TABLE dbo.OutletDimension
	DROP TABLE dbo.CardDimension
	PRINT 'Tables Dropped'
END

---------- CREATION AND INSERTION OF DIMENSION TABLES ----------

SELECT * FROM dbo.initial_dataset

-- 1A CREATION OF GROUP TABLE
CREATE TABLE GroupDimension
(
	ProductGroup VARCHAR(5) NOT NULL PRIMARY KEY,
	GroupName VARCHAR(50),
	CreateTimestamp DATETIME,
	UpdateTimestamp DATETIME
)

-- 1B INSERTION OF GROUP TABLE
INSERT INTO GroupDimension
SELECT DISTINCT ProductGroup,
GroupName,
CURRENT_TIMESTAMP AS CreateTimestamp,
CURRENT_TIMESTAMP AS UpdateTimestamp
FROM Galleria.dbo.initial_dataset

-- 2A CREATION OF NAME TABLE
CREATE TABLE NameDimension
(
	StockCode VARCHAR(50) NOT NULL PRIMARY KEY, -- Already a suitable key
	Name VARCHAR(100),
	Description VARCHAR(255),
	Price INT NOT NULL,
	CreateTimestamp DATETIME,
	UpdateTimestamp DATETIME
)

-- 2B INSERTION OF NAME TABLE
INSERT INTO NameDimension
SELECT DISTINCT StockCode,
Name,
Description,
Price,
CURRENT_TIMESTAMP AS CreateTimestamp,
CURRENT_TIMESTAMP AS UpdateTimestamp
FROM Galleria.dbo.initial_dataset


-- 3A CREATION OF OUTLET TABLE
CREATE TABLE OutletDimension
(
	OutletID INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
	Outlet VARCHAR(100),
	CreateTimestamp DATETIME,
	UpdateTimestamp DATETIME
)

-- 3B INSERTION INTO OUTLET TABLE
INSERT INTO OutletDimension
SELECT DISTINCT Outlet,
CURRENT_TIMESTAMP AS CreateTimestamp,
CURRENT_TIMESTAMP AS UpdateTimestamp
FROM Galleria.dbo.initial_dataset


-- 4A CREATION OF CARD TABLE
CREATE TABLE CardDimension
(
	CardID INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
	CardType VARCHAR(20),
	CreateTimestamp DATETIME,
	UpdateTimestamp DATETIME
)

-- 4B INSERTION INTO CARD TABLE
INSERT INTO CardDimension
SELECT DISTINCT CardType,
CURRENT_TIMESTAMP AS CreateTimestamp,
CURRENT_TIMESTAMP AS UpdateTimestamp
FROM Galleria.dbo.initial_dataset


---------- CREATION AND INSERTION OF FACT TABLE ----------

-- CREATION OF FACT TABLE
CREATE TABLE SalesFact
(
	SaleID INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
	SaleDate DATE NOT NULL,
	TicketNo INT NOT NULL,
	StockCode VARCHAR(50) NOT NULL FOREIGN KEY REFERENCES NameDimension(StockCode),
	ProductGroup VARCHAR(5) NOT NULL FOREIGN KEY REFERENCES GroupDimension(ProductGroup),
	OutletID INT NOT NULL FOREIGN KEY REFERENCES OutletDimension(OutletID),
	CardID INT NOT NULL FOREIGN KEY REFERENCES CardDimension(CardID),
	OrderQty INT NOT NULL,
	Total INT NOT NULL,
	CreateTimestamp DATETIME,
    UpdateTimestamp DATETIME

)

-- INSERTION OF FACT TABLE
INSERT INTO SalesFact
SELECT
	a.SaleDate,
	a.TicketNo,
	a.StockCode,
	a.ProductGroup,
	c.OutletID,
	d.CardID,
	a.OrderQty,
	a.Total,
	CURRENT_TIMESTAMP AS CreateTimestamp,
	CURRENT_TIMESTAMP AS UpdateTimestamp
FROM initial_dataset a
INNER JOIN GroupDimension b ON a.ProductGroup = b.ProductGroup
	INNER JOIN OutletDimension c ON a.Outlet = c.Outlet
		INNER JOIN CardDimension d ON a.CardType = d.CardType


---------- VERIFICATION ----------

-- View Tables created

SELECT *
FROM GroupDimension

SELECT *
FROM OutletDimension

SELECT *
FROM NameDimension

SELECT *
FROM CardDimension

SELECT *
FROM SalesFact

-- VERIFICATION OF SUCCRSSFUL SCHEMA
SELECT salesfact.saleid,
       salesfact.saledate,
       salesfact.ticketno,
       salesfact.stockcode,
       salesfact.orderqty,
       salesfact.total,
       namedimension.NAME,
       namedimension.description,
       namedimension.price,
       carddimension.cardtype,
       groupdimension.groupname,
       outletdimension.outlet
FROM   carddimension
       INNER JOIN salesfact
               ON carddimension.cardid = salesfact.cardid
       INNER JOIN groupdimension
               ON salesfact.productgroup = groupdimension.productgroup
       INNER JOIN namedimension
               ON salesfact.stockcode = namedimension.stockcode
       INNER JOIN outletdimension
               ON salesfact.outletid = outletdimension.outletid 
WHERE TicketNo = 92785

SELECT *
FROM initial_dataset
WHERE TicketNo = 92785

-- BY COUNt
SELECT COUNT(*) 
FROM SalesFact

SELECT COUNT(*) 
FROM NameDimension

SELECT COUNT(*) 
FROM GroupDimension

SELECT COUNT(*) 
FROM CardDimension

SELECT COUNT(*) 
FROM OutletDimension

SELECT COUNT(*) 
FROM initial_dataset

-- END
