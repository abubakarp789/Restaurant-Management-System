DESCRIBE CUSTOMER;
DESCRIBE ORDERS;
DESCRIBE ORDERDETAIL;
DESCRIBE MENUITEMTYPE;
DESCRIBE MENUITEM;
DESCRIBE PAYMENT;
DESCRIBE RATING;

SELECT * FROM Customer;
SELECT * FROM Orders;
SELECT * FROM OrderDetail;
SELECT * FROM MenuItemType;
SELECT * FROM MenuItem;
SELECT * FROM Payment;
SELECT * FROM Rating;

SELECT c.CustomerID, c.Email, o.OrderID, o.OrderDate FROM Customer c JOIN Orders o ON c.CustomerID = o.CustomerID ORDER BY c.CustomerID, o.OrderID;
SELECT c.CustomerID, c.Email, SUM(p.PaymentAmount) AS TotalAmountPaid FROM Customer c JOIN Orders o ON c.CustomerID = o.CustomerID JOIN Payment p ON o.OrderID = p.OrderID GROUP BY c.CustomerID;
SELECT PaymentMethod, SUM(PaymentAmount) AS TotalAmount FROM Payment GROUP BY PaymentMethod ORDER BY TotalAmount DESC;
SELECT m.MenuItemID,m.MenuName,AVG(r.RatingValue) AS AverageRating FROM MenuItem m JOIN Rating r ON m.MenuItemID = r.MenuItemID GROUP BY m.MenuItemID, m.MenuName ORDER BY AverageRating DESC;
SELECT c.CustomerID, c.Email, r.MenuItemID, r.RatingValue, r.Review FROM Customer c JOIN Rating r ON c.CustomerID = r.CustomerID;
SELECT m.MenuName, r.RatingValue, r.Review FROM MenuItem m JOIN Rating r ON m.MenuItemID = r.MenuItemID WHERE r.RatingValue >= 3;
SELECT c.CustomerID, c.Email,AVG(p.PaymentAmount) AS AverageOrderAmount FROM Customer c JOIN Orders o ON c.CustomerID = o.CustomerID JOIN Payment p ON o.OrderID = p.OrderID GROUP BY c.CustomerID ORDER BY AverageOrderAmount DESC;
SELECT MenuName, (SELECT AVG(RatingValue) FROM Rating WHERE MenuItemID = MenuItem.MenuItemID) AS AvgRating FROM MenuItem;
SELECT o.OrderID, c.Email, od.MenuItemID, od.Quantity FROM (SELECT OrderID, CustomerID FROM Orders) AS o JOIN Customer c ON o.CustomerID = c.CustomerID JOIN OrderDetail od ON o.OrderID = od.OrderID;
SELECT p.PaymentID, p.OrderID, p.PaymentAmount, p.PaymentDate FROM (SELECT * FROM Payment WHERE PaymentMethod = 'Credit Card') AS p;
SELECT c.CustomerID,c.Email,COUNT(o.OrderID) AS TotalOrders,SUM(od.Quantity) AS TotalItemsOrdered FROM Customer c LEFT JOIN Orders o ON c.CustomerID = o.CustomerID LEFT JOIN OrderDetail od ON o.OrderID = od.OrderID GROUP BY c.CustomerID, c.Email HAVING  COUNT(o.OrderID) >= 1 AND SUM(od.Quantity) >= 1 ORDER BY TotalOrders DESC;
