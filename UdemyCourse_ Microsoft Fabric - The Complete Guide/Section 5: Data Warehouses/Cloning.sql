

-- CLONING tables

--Create a clone of the dbo.dimension_city table.
CREATE TABLE [dbo].[dimension_city_clone] AS CLONE OF [dbo].[dimension_city];

--Create a clone of the dbo.fact_sale table.
CREATE TABLE [dbo].[fact_sale_clone] AS CLONE OF [dbo].[fact_sale];


-- Tables exist independtly
UPDATE [dbo].[dimension_city_clone]
SET City = 'NewCity'




--Create a clone of the dbo.dimension_city table in the test schema.

-- Create new schema
CREATE SCHEMA test;
CREATE TABLE [test].[dimension_city_clone] AS CLONE OF [dbo].[dimension_city];

--Create a clone of the dbo.fact_sale table in the test schema.
CREATE TABLE [test].[fact_sale_clone] AS CLONE OF [dbo].[fact_sale];



