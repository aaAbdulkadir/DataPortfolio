/***

CREATE A STAR SCHEMA BASED ON THE PLAN CREATED:

Fact Table: 
- [SalesID, SaleDate, TicketNo, Stock_Code, OutletID, CardTypeID, ProductID, NameID, OrderQty, Total] --> SalesID is primary key

Dimension Tables: 
-    - [ProductID, Product_Group, Group_name]
    - [NameID, Name, Description, Price]
    - [OutletID, Outlet]
    - [CardTypeID, CardType]

***/

CREATE DATABASE Galleria

USE Galleria
GO

-- DROP TABLE TO ENSURE CREATION IF EXISTS
BEGIN
	DROP TABLE dbo.[SalesFact]
	DROP TABLE dbo.[ProductDimension]
	DROP TABLE dbo.[NameDimension]
	DROP TABLE dbo.[OutletDimension]
	DROP TABLE dbo.[CardTypeDimension]
	PRINT 'Tables Dropped'
END

-- CREATION OF DIMENSION TABLES:

SELECT * FROM [dbo].[initial_dataset]

-- 1. PRODUCT TABLE
CREATE TABLE [ProductDimension](
	[ProductID] INT NOT NULL,
	[ProductGroup] VARCHAR(255) NOT NULL,
	[GroupName] VARCHAR(255) NOT NULL
)

-- 2. NAMES TABLE
CREATE TABLE [NameDimension](
	[NameID] INT NOT NULL,
	[Name] VARCHAR(50) NOT NULL,
	[Description] VARCHAR(255),
	[Price] FLOAT NOT NULL
)

-- 3. OUTLET TABLE
CREATE TABLE [OutletDimension](
	[OutletID] INT NOT NULL,
	[Outlet] VARCHAR(255) NOT NULL,
)

-- 4. CARD TYPE TABLE
CREATE TABLE [CardTypeDimension](
	[CardTypeID] INT NOT NULL,
	[CardType] VARCHAR(50) NOT NULL
)

-- CREATION OF FACT TABLE
CREATE TABLE [SalesFact](
	SalesID INT IDENTITY(1,1) PRIMARY KEY,
	[SaleDate] DATETIME NOT NULL,
	[TicketNo] INT NOT NULL,
	[StockCode] VARCHAR(50) NOT NULL,
	[OutletID] INT NOT NULL, 
	[CardTypeID] INT NOT NULL,
	[ProductID] INT NOT NULL,
	[NameID] INT NOT NULL,
	[OrderQty] INT NOT NULL,
	[Total] INT NOT NULL
)

/**
Once the tables have been designed with the fact table, use queries to populate tables
**/

INSERT INTO [ProductDimension]
SELECT ProductID, ProductGroup, GroupName
FROM [dbo].[initial_dataset]

INSERT INTO [NameDimension]
SELECT NameID, Name, Description, Price
FROM [dbo].[initial_dataset]

INSERT INTO [OutletDimension]
SELECT OutletID, Outlet
FROM [dbo].[initial_dataset]

INSERT INTO [CardTypeDimension]
SELECT CardTypeID, CardType
FROM [dbo].[initial_dataset]

-- Fact table
INSERT INTO [SalesFact]
(
	SaleDate, 
	OutletID,
	CardTypeID,
	ProductID,
	NameID,
	TicketNo, 
	StockCode, 
	OrderQty,
	Total
)
SELECT
	SaleDate, 
	OutletID,
	CardTypeID,
	ProductID,
	NameID,
	TicketNo, 
	StockCode, 
	OrderQty, 
	Total
FROM [dbo].[initial_dataset]

/***Add primary keys to dimension tables***/
ALTER TABLE [ProductDimension]
ADD PRIMARY KEY (ProductID)

ALTER TABLE [CardTypeDimension]
ADD PRIMARY KEY (CardTypeID)

ALTER TABLE [NameDimension]
ADD PRIMARY KEY (NameID)

ALTER TABLE [OutletDimension]
ADD PRIMARY KEY (OutletID)

/***Add foreign keys to fact table***/
ALTER TABLE [SalesFact]
ADD FOREIGN KEY (ProductID) REFERENCES ProductDimension(ProductID);

ALTER TABLE [SalesFact]
ADD FOREIGN KEY (CardTypeID) REFERENCES CardTypeDimension(CardTypeID);

ALTER TABLE [SalesFact]
ADD FOREIGN KEY (NameID) REFERENCES NameDimension(NameID);

ALTER TABLE [SalesFact]
ADD FOREIGN KEY (OutletID) REFERENCES OutletDimension(OutletID);


-- View Tables created

SELECT *
FROM [ProductDimension]

SELECT *
FROM [OutletDimension]

SELECT *
FROM [NameDimension]

SELECT *
FROM [CardTypeDimension]

SELECT *
FROM [SalesFact]

-- VERIFICATION OF SUCCRSSFUL SCHEMA
SELECT a.SalesID, a.SaleDate, a.TicketNo, a.StockCode, a.OrderQty, a.Total, b.Name, b.Price, c.CardType, d.GroupName, e.Outlet, c.CardTypeID
FROM [SalesFact] a
JOIN [NameDimension] b ON a.NameID = b.NameID
JOIN [CardTypeDimension] c ON a.CardTypeID = c.CardTypeID
JOIN [ProductDimension] d ON a.ProductID = d.ProductID
JOIN [OutletDimension] e ON a.OutletID = e.OutletID
ORDER BY TicketNo, StockCode

SELECT *
FROM initial_dataset

-- VERIFY ONE VALUE

SELECT a.SalesID, a.SaleDate, a.TicketNo, a.StockCode, a.OrderQty, a.Total, b.Name, b.Price, c.CardType, d.GroupName, e.Outlet, e.OutletID
FROM [SalesFact] a
JOIN [NameDimension] b ON a.NameID = b.NameID
JOIN [CardTypeDimension] c ON a.CardTypeID = c.CardTypeID
JOIN [ProductDimension] d ON a.ProductID = d.ProductID
JOIN [OutletDimension] e ON a.OutletID = e.OutletID
WHERE TicketNo = 92785 AND StockCode = 'PZ0019'

SELECT *
FROM initial_dataset
WHERE TicketNo = 92785 AND StockCode = 'PZ0019'

-- BY COUNt
SELECT COUNT(*) 
FROM [SalesFact]

SELECT COUNT(*) 
FROM [NameDimension]

SELECT COUNT(*) 
FROM [ProductDimension]

SELECT COUNT(*) 
FROM [CardTypeDimension]

SELECT COUNT(*) 
FROM [OutletDimension]

SELECT COUNT(*) 
FROM initial_dataset

-- END
