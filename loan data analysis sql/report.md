# Overview
The data was originally taken from the Lending Club website, which is a peer-to-peer lending company. The table from the website was modified and restructured in my previous homework to produce the table that is used in this project.  

# Table Design
inc_bracket: Is an interval of numeric values. However, no interval operations will have to be performed so we can leave the column as VARCHARS.

loan_num: This column contain a unique integer value for each record, and is should thus be an INTEGER data type, and the primary key.

loan_amnt: Numeric value that requires at most two decimal places. 

term: The values in the column come in the form of "n months", where n is a number. We can remove the "months" string from each value, and cast the numeric string. However, the values in term are not used for analysis so we left the values in their original text form. The text data type used was VAR CHAR. 

int_rate: Numeric value that requires at most two decimal places. 

installment: Numeric value that requires as most two decimal places

home_ownership: This column contains text description describing the state of home ownership. A text data type is required to represent the values so VAR CHAR was used.

annual_inc_in_1000s: Numeric value that requires as most two decimal places. 

purpose: This column contains text description describing the purpose of the loan. A text data type is required to represent the values so VAR CHAR was used.


# Import
The import succeeded without error. 
In the csv file produced from the last homework, there was a column with no column or an empty string name. That column contains unique values that were given to number the records. In the csv file, that column was given the name "loan_num".

# Database Information
\i describe.psql
```
                               List of databases
    Name    |   Owner    | Encoding | Collate |  Ctype  |   Access privileges
------------+------------+----------+---------+---------+-----------------------
 homework04 | david      | UTF8     | C.UTF-8 | C.UTF-8 |
 mydb       | mydb_admin | UTF8     | C.UTF-8 | C.UTF-8 |
 postgres   | postgres   | UTF8     | C.UTF-8 | C.UTF-8 |
 template0  | postgres   | UTF8     | C.UTF-8 | C.UTF-8 | =c/postgres          +
            |            |          |         |         | postgres=CTc/postgres
 template1  | postgres   | UTF8     | C.UTF-8 | C.UTF-8 | =c/postgres          +
            |            |          |         |         | postgres=CTc/postgres
(5 rows)
```

```

       List of relations
 Schema | Name  | Type  | Owner
--------+-------+-------+-------
 public | loans | table | david
(1 row)
```

```

                  List of relations
 Schema | Name  | Type  | Owner | Size  | Description
--------+-------+-------+-------+-------+-------------
 public | loans | table | david | 21 MB |
(1 row)
```

# Query Results

```
### 1. the total number of rows in the database

 count
--------
 100000
(1 row)
```

```
### 2. show the first 15 rows, but only display 3 columns (your choice)

 inc_bracket | loan_num | loan_amnt
-------------+----------+------------
 [0.0, 30.0) |     6012 | $28,000.00
 [0.0, 30.0) |    55016 |  $2,100.00
 [0.0, 30.0) |     6292 |  $4,200.00
 [0.0, 30.0) |    69720 | $15,175.00
 [0.0, 30.0) |    64916 | $32,050.00
 [0.0, 30.0) |    88903 | $15,000.00
 [0.0, 30.0) |    35113 |  $6,900.00
 [0.0, 30.0) |    69669 | $14,000.00
 [0.0, 30.0) |    75682 | $40,000.00
 [0.0, 30.0) |    55181 | $30,000.00
 [0.0, 30.0) |    64808 | $15,000.00
 [0.0, 30.0) |    48867 |  $7,000.00
 [0.0, 30.0) |     8486 | $32,000.00
 [0.0, 30.0) |    64697 | $20,000.00
 [0.0, 30.0) |    35415 | $24,000.00
(15 rows)
```

```
### 3. do the same as above, but chose a column to sort on, and sort in descending
### sorted on loan_num 
	
  inc_bracket  | loan_num | loan_amnt
---------------+----------+------------
 [60.0, 90.0)  |    99999 |  $5,000.00
 [30.0, 60.0)  |    99998 |  $5,000.00
 [60.0, 90.0)  |    99997 |  $4,800.00
 [90.0, 120.0) |    99996 | $12,000.00
 [120.0, inf)  |    99995 | $20,000.00
 [120.0, inf)  |    99994 | $40,000.00
 [120.0, inf)  |    99993 | $35,000.00
 [60.0, 90.0)  |    99992 | $16,925.00
 [60.0, 90.0)  |    99991 | $10,000.00
 [30.0, 60.0)  |    99990 |  $7,000.00
 [90.0, 120.0) |    99989 | $36,000.00
 [60.0, 90.0)  |    99988 | $12,000.00
 [0.0, 30.0)   |    99987 |  $7,200.00
 [60.0, 90.0)  |    99986 | $10,000.00
 [60.0, 90.0)  |    99985 | $15,000.00
(15 rows)
```

```
### 4. add a new column without a default value
ALTER TABLE
 loan_amnt_quartile
--------------------















(15 rows)
```

```
### 5. set the value of that new column
UPDATE 100000
 loan_amnt_quartile
--------------------
                  1
                  1
                  1
                  1
                  1
                  1
                  1
                  1
                  1
                  1
                  1
                  1
                  1
                  1
                  1
(15 rows)
```

```
### 6. show only the unique (non duplicates) of a column of your choice
  inc_bracket
---------------
 [60.0, 90.0)
 [120.0, inf)
 [0.0, 30.0)
 [90.0, 120.0)
 [30.0, 60.0)
(5 rows)
```

```
### 7.group rows together by a column value (your choice) and use an aggregate function to calculate something about that group 
  inc_bracket  |    avg
---------------+------------
 [60.0, 90.0)  | $16,111.73
 [120.0, inf)  | $23,126.45
 [0.0, 30.0)   | $10,257.61
 [90.0, 120.0) | $19,638.23
 [30.0, 60.0)  | $12,385.90
(5 rows)
```

```
### 8. now, using the same grouping query or creating another one, find a way to filter the query results based on the values for the groups 
 inc_bracket  | count |  avg_loan
--------------+-------+------------
 [60.0, 90.0) | 29559 | $16,111.73
 [30.0, 60.0) | 34516 | $12,385.90
(2 rows)
```

```
### 9. group rows together by home_ownership, and give count, average income, and average loan. 
 home_ownership | count |       avg_inc       | avg_loan_amnt
----------------+-------+---------------------+---------------
 MORTGAGE       | 46982 | 88.9328549231620621 |    $17,575.19
 OWN            | 13102 | 75.3059868722332468 |    $15,193.11
 RENT           | 39902 | 67.4052801864568192 |    $14,196.84
 ANY            |    14 | 54.8714285714285714 |    $12,776.79
(4 rows)
```

```
### 10. Order by loan_amnt and display the 10 highest loans. 
  inc_bracket  | loan_num | loan_amnt |    term    | int_rate | installment | home_ownership | annual_inc_in_1000s |      purpose       | loan_amnt_quartile
---------------+----------+-----------+------------+----------+-------------+----------------+---------------------+--------------------+--------------------
 [60.0, 90.0)  |    94398 |  40000.00 |  36 months |    10.41 |     1298.41 | MORTGAGE       |               80.00 | debt_consolidation |                  4
 [120.0, inf)  |    59061 |  40000.00 |  60 months |     7.46 |      800.76 | MORTGAGE       |              130.00 | debt_consolidation |                  4
 [90.0, 120.0) |    48234 |  40000.00 |  60 months |    16.46 |      982.53 | MORTGAGE       |               90.00 | debt_consolidation |                  4
 [120.0, inf)  |    77393 |  40000.00 |  60 months |    10.90 |      867.71 | MORTGAGE       |              308.00 | home_improvement   |                  4
 [60.0, 90.0)  |    64609 |  40000.00 |  60 months |     7.46 |      800.76 | MORTGAGE       |               69.50 | debt_consolidation |                  4
 [90.0, 120.0) |    91133 |  40000.00 |  60 months |     7.34 |      798.49 | MORTGAGE       |              117.00 | debt_consolidation |                  4
 [90.0, 120.0) |    40909 |  40000.00 |  60 months |     9.92 |      848.31 | MORTGAGE       |               97.00 | credit_card        |                  4
 [90.0, 120.0) |    72208 |  40000.00 |  60 months |     7.34 |      798.49 | OWN            |               95.00 | debt_consolidation |                  4
 [90.0, 120.0) |    61898 |  40000.00 |  36 months |     6.07 |     1218.15 | MORTGAGE       |              100.00 | debt_consolidation |                  4
 [90.0, 120.0) |    63941 |  40000.00 |  36 months |    12.13 |     1331.06 | RENT           |              101.00 | other              |                  4
 [90.0, 120.0) |    96024 |  40000.00 |  60 months |    10.90 |      867.71 | MORTGAGE       |              105.00 | home_improvement   |                  4
 [120.0, inf)  |     8329 |  40000.00 |  60 months |    10.07 |      851.27 | MORTGAGE       |              500.00 | debt_consolidation |                  4
 [120.0, inf)  |    33346 |  40000.00 |  36 months |    10.07 |     1292.01 | MORTGAGE       |              140.00 | small_business     |                  4
 [60.0, 90.0)  |    94183 |  40000.00 |  36 months |     5.31 |     1204.42 | MORTGAGE       |               60.00 | debt_consolidation |                  4
 [120.0, inf)  |     3514 |  40000.00 |  36 months |     5.31 |     1204.42 | MORTGAGE       |              400.00 | credit_card        |                  4
(15 rows)
```

```
### 11. Group by the purpose for the loan, and display the average loan and count for each group.
      purpose       |  avg_loan  | count
--------------------+------------+-------
 vacation           |  $6,954.51 |   860
 moving             |  $9,746.77 |   735
 car                | $10,406.94 |  1163
 medical            | $11,572.64 |  1439
 other              | $12,062.87 |  8286
 renewable_energy   | $12,642.50 |    60
 major_purchase     | $15,067.86 |  2837
 credit_card        | $15,504.50 | 25649
 home_improvement   | $15,813.00 |  7260
 house              | $16,318.91 |  1675
 debt_consolidation | $17,261.56 | 49118
 small_business     | $20,058.80 |   918
(12 rows)
```

```
### 12. write a comment about your query 12
  inc_bracket  | avg_int_rate | count
---------------+--------------+-------
 [120.0, inf)  | 11.55%       | 14479
 [90.0, 120.0) | 12.07%       | 14162
 [60.0, 90.0)  | 12.51%       | 29559
 [30.0, 60.0)  | 13.09%       | 34516
 [0.0, 30.0)   | 13.72%       |  7284
(5 rows)
```
