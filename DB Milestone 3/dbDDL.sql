DROP DATABASE Kamal_Restaurant;
CREATE DATABASE Kamal_Restaurant;
USE Kamal_Restaurant;

CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    Email VARCHAR(50), 
    Phone VARCHAR(20), 
    Address VARCHAR(100)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT,
    OrderDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

CREATE TABLE MenuItemType (
    MenuItemTypeID INT PRIMARY KEY AUTO_INCREMENT,
    TypeName VARCHAR(50)
);

CREATE TABLE MenuItem (
    MenuItemID INT PRIMARY KEY AUTO_INCREMENT,
    MenuName VARCHAR(50),
    Price DECIMAL(10, 2),
    Description VARCHAR(255),
    MenuItemTypeID INT,
    FOREIGN KEY (MenuItemTypeID) REFERENCES MenuItemType(MenuItemTypeID)
);

CREATE TABLE OrderDetail (
    OrderDetailID INT PRIMARY KEY AUTO_INCREMENT,
    OrderID INT,
    MenuItemID INT,
    Quantity INT,
    SpecialInstructions VARCHAR(255),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (MenuItemID) REFERENCES MenuItem(MenuItemID)
);

CREATE TABLE Payment (
    PaymentID INT PRIMARY KEY AUTO_INCREMENT,
    OrderID INT,
    PaymentAmount DECIMAL(10, 2),
    PaymentDate DATE,
    PaymentMethod VARCHAR(50),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

CREATE TABLE Rating (
    RatingID INT PRIMARY KEY AUTO_INCREMENT,
    MenuItemID INT,
    RatingValue INT CHECK (RatingValue BETWEEN 1 AND 5),
    Review VARCHAR(255),
    CustomerID INT,
    FOREIGN KEY (MenuItemID) REFERENCES MenuItem(MenuItemID),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);




