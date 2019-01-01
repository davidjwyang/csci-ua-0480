-- write your table creation sql here!
DROP TABLE IF EXISTS loans;


CREATE TABLE loans (
	inc_bracket VARCHAR NOT NUll,
	loan_num INTEGER PRIMARY KEY,
	loan_amnt NUMERIC(18,2) NOT NULL,
	term VARCHAR NOT NULL,
	int_rate NUMERIC(18,2) NOT NULL,
	installment NUMERIC(18,2) NOT NULL,
	home_ownership VARCHAR NOT NULL,
	annual_inc_in_1000s NUMERIC(18,2) NOT NULL,
	purpose VARCHAR NOT NULL 
);

