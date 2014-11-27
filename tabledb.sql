CREATE TABLE Media (
   ID INTEGER PRIMARY KEY     AUTOINCREMENT,
   DATE           TEXT    NOT NULL,
   CAMPAIGN       TEXT     NOT NULL,
   PRODUCT        CHAR(180),
   PLACEMENT      CHAR(180),
   CREATIVE       CHAR(180),
   CLICKS         INT,   
   IMPRESSIONS    INT,
   SALES          INT,   
   COST           REAL,
   CTR            REAL,  
   CR             REAL,  
   CPA            REAL      
);