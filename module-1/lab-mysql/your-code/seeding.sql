
INSERT INTO Cars (VIN, Manufacturer, Model, Year, Color)
VALUES 
("3K096I98581DHSNUP", "Volkswagen", "Tiguan", "2019", "Blue"),
("ZM8G7BEUQZ97IH46V",	"Peugeot",	"Rifter",	"2019",	"Red"),
("RKXVNNIHLVVZOUB4M",	"Ford",		"Fusion",	"2018",	"White"),
("HKNDGS7CU31E9Z7JW",	"Toyota",	"RAV4",	"2018",	"Silver"),
("DAM41UDN3CHU2WVF6",	"Volvo",	"V60",	"2019",	"Gray"),
("DAM41UDN3CHU2WVF6",	"Volvo",	"V60 Cross Country",	"2019",	"Gray");


INSERT INTO Customers (Customers_id, Name, Phone, Email, Adress, City, State_Province, Country, Postal, Invoices_ID_Invoices) 
VALUES
 ("10001", "Pablo Picasso", "+34 636 17 63 82", null, "Paseo de la Chopera, 14", "Madrid", "Madrid", "Spain", "28045", null),
("20001", "Abraham Lincoln", "+1 305 907 7086", null, "120 SW 8th St", "Miami", "Florida", "Unnited States", "33130", null),
("30001", "Napoleon Bonaparte", "+33 1 79 75 40 00", null, "40 Rue du Colisée", "Paris", "Île-de-France", "France", "75008", null);

INSERT INTO Salespersons (Staff_ID, Name, Store, Invoices_ID_Invoices) VALUES ("00001","Petey Cruiser", "Madrid", null), ("00002", "Anna Sthesia", "Barcelona", null), ("00003", "Paul Molive", "Berlin", null),
("00004", "Gail Forcewind", "Paris", null), ("0005", "Paige Turner", "Mimia",null), ("00006", "Bob Frapples", "Mexico City", null), ("00007", "Walter Melon", "Amsterdam", null),
("00008", "Shonda Leer","São Paulo", null);
INSERT INTO Invoices (invoicenumber, Date, Car, Customer, SalesPerson, Cars_ID_Cars) VALUES ("852399038", "20180822",  "0", "1", "3", null), ("731166526","20181231", "3", "0", "5", null), 
("271135104", "20190122", "2", "2", "7", null);	

