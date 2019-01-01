-- write your queries underneath each number:
 
-- 1. the total number of rows in the database
SELECT COUNT(*) 
FROM loans;

-- 2. show the first 15 rows, but only display 3 columns (your choice)
SELECT inc_bracket, loan_num, loan_amnt::MONEY 
FROM loans 
LIMIT 15; 

-- 3. do the same as above, but chose a column to sort on, and sort in descending order
--- sorted on the 'loan_num'
SELECT inc_bracket, loan_num, loan_amnt::MONEY 
FROM loans 
ORDER BY loan_num DESC
LIMIT 15;

-- 4. add a new column without a default value
ALTER TABLE loans
ADD COLUMN loan_amnt_quartile INTEGER;

SELECT loan_amnt_quartile
FROM loans 
LIMIT 15;

-- 5. set the value of that new column
UPDATE loans as l
SET loan_amnt_quartile = s.loan_amnt_quartile
FROM (SELECT loan_num, ntile(4) over (ORDER BY loan_amnt) as loan_amnt_quartile
FROM loans) as s
WHERE l.loan_num = s.loan_num;

SELECT loan_amnt_quartile
FROM loans
LIMIT 15;	

-- 6. show only the unique (non duplicates) of a column of your choice
SELECT DISTINCT inc_bracket   
FROM loans;

--7.group rows together by a column value (your choice) and use an aggregate function to calculate something about that group 
SELECT inc_bracket, AVG(loan_amnt)::NUMERIC::MONEY, COUNT(*)
FROM loans
GROUP BY inc_bracket;

-- 8. now, using the same grouping query or creating another one, find a way to filter the query results based on the values for the groups 
SELECT inc_bracket, COUNT(*) as count, AVG(loan_amnt)::NUMERIC::MONEY as avg_loan 
FROM loans
GROUP BY inc_bracket
HAVING COUNT(*)>20000;	

-- 9. group rows together by home_ownership, and give count, average income, and average loan. 
SELECT home_ownership, COUNT(*), AVG(annual_inc_in_1000s) as avg_inc, AVG(loan_amnt)::NUMERIC::MONEY as avg_loan_amnt 
FROM loans
GROUP BY home_ownership; 

-- 10. Order by loan_amnt and display the 15 highest loans. 
SELECT * 
FROM loans
ORDER BY loan_amnt DESC
LIMIT 15;

-- 11. Group by the purpose for the loan, and display the average loan and count for each group.
SELECT purpose, AVG(loan_amnt)::NUMERIC::MONEY as avg_loan, COUNT(*) as count
FROM loans
GROUP BY purpose
ORDER BY AVG(loan_amnt);

-- 12. Group by income brackets, and order by and display the average interest rate and count 
-- for each group. 
SELECT inc_bracket, AVG(int_rate)::NUMERIC(5,2)::VARCHAR||'%' as avg_int_rate, COUNT(*) as count 
FROM loans
GROUP BY inc_bracket
ORDER BY AVG(int_rate);