CREATE DATABASE Apteka;

USE Apteka;

CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(64),
    password VARCHAR(64),
    role VARCHAR(32) DEFAULT 'user'
);

insert into users (login, password) values ('Niki', 1621);
insert into users (login, password) values ('Lila', 4681);
insert into users (login, password) values ('Marrissa', 2135);
insert into users (login, password) values ('Robbie', 1399);
insert into users (login, password) values ('Belicia', 2669);

UPDATE Users
SET role = 'admin'
WHERE id LIKE 2;

UPDATE users
SET phone_number = '+998937771053'
WHERE id LIKE 1;

UPDATE users
SET phone_number = '+998977775153'
WHERE id LIKE 2;

UPDATE users
SET phone_number = '+998996535753'
WHERE id LIKE 4;

UPDATE users
SET phone_number = '+998901251053'
WHERE id LIKE 6;

CREATE TABLE Suppliers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(64),
    phone_number VARCHAR(13)
);

INSERT INTO Suppliers (name, phone_number) VALUES ('OOO "FAMILY PHARMA"','+998712125247');
INSERT INTO Suppliers (name, phone_number) VALUES ('OOO «DRUG-PROMOTION»','+998712152451');
INSERT INTO Suppliers (name, phone_number) VALUES ('OOO MEROS PHARM TASHKENT','+998771254587');
INSERT INTO Suppliers (name, phone_number) VALUES ('OOO Curatio Pharm','+998781254633');

CREATE TABLE customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(64),
    date DATE DEFAULT '2024-08-04',
    amount INT DEFAULT 100000,
    phone_number VARCHAR(13),
    address VARCHAR(64)
);

INSERT INTO customer (name, date, phone_number, address) VALUES ('Ali','2024-11-04','+974030271','Amir Temur 123');

CREATE TABLE medics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(64),
    category VARCHAR(64),
    input_price INT,
    output_price INT,
    amount INT,
    image VARCHAR(256)
);

INSERT INTO medics (name, category, input_price, output_price, amount, image) VALUES ('Paracetamol','Tabletka',1200,2000,50,'paracetamol.png');
INSERT INTO medics (name, category, input_price, output_price, amount, image) VALUES ('Fanigan-fast gel','Maz',4100,5500,55,'fanigan.png');
INSERT INTO medics (name, category, input_price, output_price, amount, image) VALUES ('Analgin','Tabletka',60000,75000,65,'analgin.png');
INSERT INTO medics (name, category, input_price, output_price, amount, image) VALUES ('Ugol','Tabletka',650,800,72,'ugol.png');
INSERT INTO medics (name, category, input_price, output_price, amount, image) VALUES ('Surol','Tabletka',475000,500000,47,'surol.png');