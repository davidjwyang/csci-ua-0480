CREATE TABLE customers(
	email VARCHAR,
	first_name VARCHAR NOT NULL,
	last_name VARCHAR NOT NULL,
	cell_phone_num VARCHAR	NOT NULL,
	address VARCHAR	NOT NULL,
	date_of_regist DATE	NOT NULL,
	payment_info VARCHAR NOT NULL,
	referral VARCHAR, 
	flag BOOLEAN,
	-- Borrow_id will reference a currently standing borrow transacton. In other words
	-- the scooter has been borrowed but has not been returned yet. 
	
	PRIMARY KEY (email),
	FOREIGN KEY (referral) REFERENCES customers (email),
);

CREATE TABLE inventory(
	id SERIAL, 
	scooter_id INTEGER NOT NULL,
	customer_email VARCHAR, --null if no customer has the scooter.
	condition VARCHAR NOT NULL,

	PRIMARY KEY (id),
	FOREIGN KEY (scooter_id) REFERENCES scooters (id),
	FOREIGN KEY (customer_email) REFERENCES customers (email)-- should we keep?
);

CREATE TABLE scooters(
	id SERIAL,
	manufacturer VARCHAR NOT NULL,
	model_number INTEGER NOT NULL,
	range (km) NUMERIC(8,2) NOT NULL,
	weight (kg) NUMERIC(8,2) NOT NULL,
	top_speed (km/h) NUMERIC(8,2) NOT NULL,
	
	PRIMARY KEY (id),
	FOREIGN KEY (manufacturer) REFERENCES manufacturers (manufacturer)
);

CREATE TABLE manufacturers(
	manufacturer VARCHAR,
	country VARCHAR NOT NULL, 

	PRIMARY KEY (manufacturer)
);

CREATE TABLE borrows(
	id SERIAL, 
	customer_email VARCHAR NOT NULL,
	item_id INTEGER NOT NULL,
	checked_out TIMESTAMP NOT NULL,
	due TIMESTAMP NOT NULL,
	payment_amount MONEY NOT NULL,
	return_id INTEGER, 
	late BOOLEAN,
	return_time TIMESTAMP,

	PRIMARY KEY (id),
	FOREIGN KEY (customer_email) REFERENCES customers (id),
	FOREIGN KEY (item_id) REFERENCES inventory (id),
);

CREATE TABLE fees( 
	id SERIAL, 
	borrow_id INTEGER, 
	type VARCHAR NOT NULL,
	amount MONEY NOT NULL,
	payed BOOLEAN NOT NULL,

	PRIMARY KEY (id),
	FOREIGN KEY (borrow_id) references borrow (id)
)

CREATE TABLE notes(
	id SERIAL,
	borrow_id INTEGER,
	type VARCHAR,
	note TEXT
)