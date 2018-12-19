/* Author: Liam McCann
 * filename: teamtable.sql
 * project: Mock Database
 * functionality: schema for nba teams
 */
 
CREATE TABLE TEAMS(
	ID INT PRIMARY KEY NOT NULL,
	NAME VARCHAR(30) NOT NULL,
	STATE VARCHAR(30) NULL,
	CITY VARCHAR(30) NULL,
	RECORD VARCHAR(10) NOT NULL
);
