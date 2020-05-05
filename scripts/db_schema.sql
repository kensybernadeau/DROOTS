CREATE TABLE Users(user_id serial PRIMARY KEY, user_first_name VARCHAR(10), user_last_name VARCHAR(20), user_uname VARCHAR(10),user_password VARCHAR(10))

CREATE TABLE Administrators(admin_id serial PRIMARY KEY, user_id INTEGER REFERENCES Users(user_id))

CREATE TABLE Customer(customer_id serial PRIMARY KEY, user_id INTEGER REFERENCES Users(user_id))

CREATE TABLE Address(address_id serial primary key,user_country varchar(20),user_city varchar(20),user_street_address varchar(50),user_zipcode integer, user_id integer REFERENCES Users(user_id))

CREATE TABLE Suppliers(supplier_id serial PRIMARY KEY,user_id INTEGER REFERENCES Users(user_id))

CREATE TABLE  Supplies( supplies_price FLOAT, supplies_stock INTEGER, supplier_id INTEGER REFERENCES Suppliers(supplier_id), resource_id INTEGER REFERENCES Resources(resource_id), PRIMARY KEY(supplier_id, resource_id))

CREATE TABLE  Resources(resource_id  serial PRIMARY KEY, resource_name VARCHAR(20) , resource_category VARCHAR (20))

CREATE TABLE Ice(ice_id serial PRIMARY KEY, ice_description VARCHAR(250), resource_id INTEGER references resources(resource_id))

CREATE TABLE Water(water_id serial PRIMARY KEY, water_oz INTEGER, water_type VARCHAR(10),resource_id INTEGER references resources(resource_id))

CREATE TABLE  Clothing(clothe_id serial PRIMARY KEY, clothe_type VARCHAR(14) , clothe_size VARCHAR(10) , clothe_description VARCHAR(250) , resource_id INTEGER REFERENCES Resources(resource_id))

CREATE TABLE  Tools(tool_id serial PRIMARY KEY, tool_name VARCHAR(10), tool_description VARCHAR(250) , resource_id INTEGER REFERENCES Resources(resource_id))

CREATE TABLE Health(health_id serial PRIMARY KEY, health_type VARCHAR(15), health_exp_date CHAR(10), health_description VARCHAR(250), resource_id  INTEGER REFERENCES resources(resource_id))

CREATE TABLE Food(food_id serial PRIMARY KEY, food_exp_date VARCHAR10), food_type VARCHAR(15), food_description VARCHAR(250), resource_id INTEGER references resources(resource_id))

CREATE TABLE Power_Resources(power_id serial PRIMARY KEY,power_type VARCHAR(10),power_description VARCHAR(250), resource_id INTEGER REFERENCES Resources(resource_id))

CREATE TABLE Fuel(fuel_id serial PRIMARY KEY,fuel_type VARCHAR(10),fuel_liters INTEGER,resource_id INTEGER REFERENCES Resources(resource_id))

CREATE TABLE Heavy_Equipment(heavy_id serial PRIMARY KEY, heavy_description VARCHAR(50), resource_id REFERENCES Resources(resource_id) )

CREATE TABLE Batteries (batteries_id serial PRIMARY KEY, batteries_material VARCHAR(20), batteries_voltage VARCHAR(10), battery_type VARCHAR(10), battery_description VARCHAR(50), resource_id INTEGER REFERENCES Resources(resource_id))

CREATE TABLE Request(request_id serial PRIMARY KEY, customer_id REFERENCES Customer(customer_id), resource_id INTEGER REFERENCES resources(resource_id))

CREATE TABLE Reservation(reservation_id serial PRIMARY KEY, customer_id REFERENCES Customer(customer_id), resource_id INTEGER, supplier_id INTEGER, FOREIGN KEY (supplier_id, resource_id) REFERENCES supplies(supplier_id, resource_id))

CREATE TABLE Payment(payment_id serial PRIMARY KEY, payment_date VARCHAR(20), payment_amount FLOAT,resource_id INTEGER, supplier_id INTEGER, FOREIGN KEY (supplier_id, resource_id) REFERENCES supplies(supplier_id, resource_id))

CREATE TABLE athmovil( athmovil_id serial PRIMARY KEY, athmovil_transaction_num VARCHAR(20), athmovil_phone_number VARCHAR(20), payment_id REFERENCES Payment(payment_id))

CREATE TABLE Card(card_id serial PRIMARY KEY, card_type VARCHAR(20), card_number INTEGER, card_secutrity_code INTEGER(3), payment_id REFERENCES Payment(payment_id))

