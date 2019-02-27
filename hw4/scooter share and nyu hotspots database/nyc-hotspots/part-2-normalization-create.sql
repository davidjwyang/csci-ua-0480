DROP TABLE IF EXISTS hotspots;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS boroughs;
DROP TABLE IF EXISTS providers_ssids;
DROP TABLE IF EXISTS ssids;
DROP TABLE IF EXISTS providers;

CREATE TABLE providers(
	name VARCHAR,

	PRIMARY KEY (name)
);

CREATE TABLE ssids(
	ssid VARCHAR,    

	PRIMARY KEY (ssid)                                  
);

CREATE TABLE providers_ssids(
	provider VARCHAR,
	ssid VARCHAR,

	PRIMARY KEY (provider, ssid),
	FOREIGN KEY (provider) REFERENCES providers(name),
	FOREIGN KEY (ssid) REFERENCES ssids(ssid)
);

CREATE TABLE boroughs(
	name VARCHAR,
	code INTEGER,

	PRIMARY KEY (name)
);

CREATE TABLE cities(
	id SERIAL,
	name VARCHAR,
	boro VARCHAR,

	PRIMARY KEY (id),
	FOREIGN KEY (boro) REFERENCES boroughs (name)
);

CREATE TABLE locations(
	lat FLOAT,
	long FLOAT,
	coun_dist INTEGER,
	post_code VARCHAR,
	city_id INTEGER,
	
	PRIMARY KEY (lat, long),	
	FOREIGN KEY (city_id) REFERENCES cities(id)
);

CREATE TABLE hotspots(
	id INTEGER,
	type VARCHAR, 
	remarks VARCHAR,
	activated DATE,
	bin VARCHAR,
	bbl VARCHAR,
	setting_descrip VARCHAR,
	setting_type VARCHAR,
	provider VARCHAR,
	lat FLOAT,
	long FLOAT,

	PRIMARY KEY (id),
	FOREIGN KEY (provider) REFERENCES providers(name),
	FOREIGN KEY (lat, long) REFERENCES locations(lat, long)
);