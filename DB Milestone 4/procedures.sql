DELIMITER //

CREATE PROCEDURE InsertCustomer(IN p_email VARCHAR(50), IN p_phone VARCHAR(20), IN p_address VARCHAR(100)) BEGIN INSERT INTO Customer (Email, Phone, Address) VALUES (p_email, p_phone, p_address); END //

CREATE PROCEDURE UpdateCustomer(IN p_customer_id INT, IN p_email VARCHAR(50), IN p_phone VARCHAR(20), IN p_address VARCHAR(100)) BEGIN UPDATE Customer SET Email = p_email, Phone = p_phone, Address = p_address WHERE CustomerID = p_customer_id; END //

CREATE PROCEDURE DeleteCustomer(IN p_customer_id INT) BEGIN DELETE FROM Customer WHERE CustomerID = p_customer_id; END //

CREATE PROCEDURE SearchCustomersByEmail(IN p_email VARCHAR(50)) BEGIN SELECT * FROM Customer WHERE Email LIKE CONCAT('%', p_email, '%'); END //

CREATE PROCEDURE InsertOrder(IN p_CustomerID INT, IN p_OrderDate DATE) BEGIN INSERT INTO Orders (CustomerID, OrderDate) VALUES (p_CustomerID, p_OrderDate); END //

CREATE PROCEDURE UpdateOrder(IN p_OrderID INT, IN p_CustomerID INT, IN p_OrderDate DATE) BEGIN UPDATE Orders SET CustomerID = p_CustomerID, OrderDate = p_OrderDate WHERE OrderID = p_OrderID; END //

CREATE PROCEDURE DeleteOrder(IN p_OrderID INT) BEGIN DELETE FROM Orders WHERE OrderID = p_OrderID; END //

CREATE PROCEDURE SearchOrdersByCustomerID(IN p_CustomerID INT) BEGIN SELECT * FROM Orders WHERE CustomerID = p_CustomerID; END //

CREATE PROCEDURE InsertMenuItemType(IN type_name VARCHAR(50)) BEGIN INSERT INTO MenuItemType (TypeName) VALUES (type_name); END //

CREATE PROCEDURE UpdateMenuItemType(IN type_id INT, IN type_name VARCHAR(50)) BEGIN UPDATE MenuItemType SET TypeName = type_name WHERE MenuItemTypeID = type_id; END //

CREATE PROCEDURE DeleteMenuItemType(IN type_id INT) BEGIN DELETE FROM MenuItemType WHERE MenuItemTypeID = type_id; END //

CREATE PROCEDURE SearchMenuItemTypes() BEGIN SELECT * FROM MenuItemType; END //

CREATE PROCEDURE InsertMenuItem(IN menu_name VARCHAR(50), IN price DECIMAL(10, 2), IN description VARCHAR(255), IN type_id INT) BEGIN INSERT INTO MenuItem (MenuName, Price, Description, MenuItemTypeID) VALUES (menu_name, price, description, type_id); END //

CREATE PROCEDURE UpdateMenuItem(IN item_id INT, IN menu_name VARCHAR(50), IN price DECIMAL(10, 2), IN description VARCHAR(255), IN type_id INT) BEGIN UPDATE MenuItem SET MenuName = menu_name, Price = price, Description = description, MenuItemTypeID = type_id WHERE MenuItemID = item_id; END //

CREATE PROCEDURE DeleteMenuItem(IN item_id INT) BEGIN DELETE FROM MenuItem WHERE MenuItemID = item_id; END //

CREATE PROCEDURE SearchMenuItemsByMenuItemTypeID(IN type_id INT) BEGIN SELECT * FROM MenuItem WHERE MenuItemTypeID = type_id; END //

CREATE PROCEDURE InsertOrderDetail(IN order_id INT, IN item_id INT, IN quantity INT, IN instructions VARCHAR(255)) BEGIN INSERT INTO OrderDetail (OrderID, MenuItemID, Quantity, SpecialInstructions) VALUES (order_id, item_id, quantity, instructions); END //

CREATE PROCEDURE UpdateOrderDetail(IN detail_id INT, IN order_id INT, IN item_id INT, IN quantity INT, IN instructions VARCHAR(255)) BEGIN UPDATE OrderDetail SET OrderID = order_id, MenuItemID = item_id, Quantity = quantity, SpecialInstructions = instructions WHERE OrderDetailID = detail_id; END //

CREATE PROCEDURE DeleteOrderDetail(IN detail_id INT) BEGIN DELETE FROM OrderDetail WHERE OrderDetailID = detail_id; END //

CREATE PROCEDURE SearchOrderDetailsByOrderID(IN order_id INT) BEGIN SELECT * FROM OrderDetail WHERE OrderID = order_id; END //

CREATE PROCEDURE InsertPayment(IN order_id INT, IN amount DECIMAL(10, 2), IN pay_date DATE, IN method VARCHAR(50)) BEGIN INSERT INTO Payment (OrderID, PaymentAmount, PaymentDate, PaymentMethod) VALUES (order_id, amount, pay_date, method); END //

CREATE PROCEDURE UpdatePayment(IN payment_id INT, IN order_id INT, IN amount DECIMAL(10, 2), IN pay_date DATE, IN method VARCHAR(50)) BEGIN UPDATE Payment SET PaymentAmount = amount, PaymentDate = pay_date, PaymentMethod = method WHERE PaymentID = payment_id AND orderID = order_id; END //

CREATE PROCEDURE DeletePayment(IN payment_id INT) BEGIN DELETE FROM Payment WHERE PaymentID = payment_id; END //

CREATE PROCEDURE SearchPaymentsByOrderID(IN order_id INT) BEGIN SELECT * FROM Payment WHERE OrderID = order_id; END //

CREATE PROCEDURE InsertRating(IN item_id INT, IN rating_value INT, IN review VARCHAR(255), IN cust_id INT) BEGIN INSERT INTO Rating (MenuItemID, RatingValue, Review, CustomerID) VALUES (item_id, rating_value, review, cust_id); END //

CREATE PROCEDURE UpdateRating(IN rating_id INT, IN menu_item_id INT, IN rating_value INT, IN review VARCHAR(255), IN customer_id INT) BEGIN UPDATE Rating SET MenuItemID = menu_item_id, RatingValue = rating_value, Review = review, CustomerID = customer_id WHERE RatingID = rating_id; END //

CREATE PROCEDURE DeleteRating(IN rating_id INT) BEGIN DELETE FROM Rating WHERE RatingID = rating_id; END //

CREATE PROCEDURE SearchRatingsByMenuItemID(IN item_id INT) BEGIN SELECT * FROM Rating WHERE MenuItemID = item_id; END //

DELIMITER ;
