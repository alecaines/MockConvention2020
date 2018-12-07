/*
 * Author: Ruinan Liu "Alan"
 * Filename: demographictables
 * Project: Mock Convention
 * Functionality: This files create the tables for region, state, county, precinct
 */

 CREATE TABLE REGION(
   regionID INT NOT NULL,
   regionName VARCHAR(20) NOT NULL,
   PRIMARY KEY (regionID)
 );


 CREATE TABLE STATE(
   stateID INT NOT NULL,
   regionID INT NOT NULL,
   stateName VARCHAR(20) NOT NULL,
   PRIMARY KEY (stateID),
   FOREIGN KEY (stateID) REFERENCES REGION(regionID)
 );


 CREATE TABLE COUNTY(
   countyID INT NOT NULL,
   stateID INT NOT NULL
   countyName VARCHAR(20) NOT NULL,
   population INT NOT NULL,
   income INT NOT NULL,
   education FLOAT NOT NULL,
   lastElectionParty VARCHAR(20) NOT NULL,
   lastElectionCandidate VARCHAR(20) NOT NULL,
   PRIMARY KEY (countyID),
   FOREIGN KEY (countyID) REFERENCES STATE(stateID)
 );


 CREATE TABLE PRECINCT(
   precinctID INT NOT NULL,
   countyID INT NOT NULL,
   precinctName VARCHAR(20) NOT NULL,
   PRIMARY KEY (precinctID),
   FOREIGN KEY (precinctID)  REFERENCES COUNTY(countyID)
 );
