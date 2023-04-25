-- SQL-команды для создания таблиц
CREATE DATABASE north;

CREATE TABLE employees
(
	first_name varchar(20) NOT NULL,
	last_name varchar(30) NOT NULL,
	title varchar(25) NOT NULL,
	birth_date date NOT NULL,
	notes text
);

CREATE TABLE customers
(
	customer_id varchar(15) PRIMARY KEY,
	company_name varchar(40) NOT NULL,
	contact_name varchar(25)
);

CREATE TABLE orders
(
	odrer_id int PRIMARY KEY,
	customer_id varchar(15) REFERENCES customers(customer_id) NOT NULL,
	employee_id int NOT NULL,
	order_date date NOT NULL,
	ship_city varchar(20) NOT NULL
);
