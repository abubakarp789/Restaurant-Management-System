# Food Management System

The Food Management System is a comprehensive Python application designed to streamline various aspects of restaurant operations. It includes functionalities for managing menu items, order details, payments, and customer ratings. The application features a graphical user interface (GUI) built with Tkinter and uses MySQL for efficient data storage.

## Functionality

### Customer Table

- **Add Customer**: Allows adding a new customer to the database.
- **Update Customer**: Updates existing customer information such as name, email, or phone number.
- **Delete Customer**: Removes a customer from the database.
- **Search Customer**: Retrieves customer information based on name, email, or phone number.

### Orders Table

- **Place Order**: Records a new order with details such as customer ID and order date.
- **Update Order**: Allows updating order details such as customer ID or order date.
- **Cancel Order**: Removes an order and associated details from the database.
- **Search Order**: Retrieves orders based on order ID or customer ID.

### MenuItemType Table

- **Add Menu Item Type**: Introduces a new category (e.g., Appetizer, Main Course) for menu items.
- **Update Menu Item Type**: Modifies existing menu item types, such as changing the name.
- **Delete Menu Item Type**: Removes a menu item type and reassigns its items to another type if applicable.
- **Search Menu Item Type**: Retrieves menu item types based on type ID or type name.

### MenuItem Table

- **Add Menu Item**: Introduces a new menu item with details like type ID, name, and price.
- **Update Menu Item**: Modifies existing menu items by changing their name, price, or type.
- **Delete Menu Item**: Removes a menu item from the database.
- **Search Menu Item**: Retrieves menu items based on item ID, name, type, or price range.

### OrderDetail Table

- **Add Order Detail**: Records details of items included in an order, such as menu item ID and quantity.
- **Update Order Detail**: Modifies existing order details like item quantity or special instructions.
- **Delete Order Detail**: Removes specific item details from an order.
- **Search Order Detail**: Retrieves order details based on order ID or menu item ID.

### Payment Table

- **Record Payment**: Logs details of a payment including order ID, amount, date, and payment method.
- **Update Payment**: Modifies payment details such as amount, date, or method.
- **Delete Payment**: Removes a payment record from the database.
- **Search Payment**: Retrieves payments based on payment ID, order ID, or date range.

### Rating Table

- **Record Rating**: Captures feedback from customers about menu items, including rating (1 to 5 stars) and review text.
- **Update Rating**: Modifies existing ratings by changing the rating value or review text.
- **Delete Rating**: Removes a rating and associated feedback from the database.
- **Search Rating**: Retrieves ratings based on rating ID, menu item ID, customer ID, or rating value.

## System Requirements

### Software Requirements
- Python 3.x
- VS Code (Any code editor)
- MySQL Server
- MySQL Connector/Python

### Hardware Requirements
- A standard desktop or laptop capable of running Python applications.

## Installation Instructions

1. **Install Python**:
   - Download and install Python 3.x from [python.org](https://www.python.org/).

2. **Install MySQL Server**:
   - Download and install MySQL Server from [mysql.com](https://www.mysql.com/) if not already installed.

3. **Install Required Python Libraries**:
   - Open a terminal or command prompt.
   - Install MySQL Connector/Python:
     ```bash
     pip install mysql-connector-python
     ```
   - Install Tkinter (if not included):
     ```bash
     pip install tk
     ```


## Usage Instructions

### Running the Application
1. Navigate to the project directory.
2. Start the application:
   ```bash
   python main.py
   ```

### Using the Application
- Navigate through different modules (Customer Management, Menu Item Management, Order Detail Management, Payment Management, Rating Management) using the GUI.
- Perform operations such as adding, updating, deleting, and searching data.
- Efficiently view and manage restaurant data through intuitive interfaces.

## Code Structure Overview

- **customer_management.py**: Manages customer operations including CRUD operations.
- **order_management.py**: Manages order operations including CRUD operations.
- **menu_item_type_management.py**: Manages menu item type operations including CRUD operations.
- **menu_item_management.py**: Handles GUI and database operations for menu items.
- **order_detail_management.py**: Manages order details including CRUD operations.
- **payment_management.py**: Controls payment functionalities.
- **rating_management.py**: Manages customer ratings and reviews.

## Database Schema

### Customer Table
- **CustomerID**: Unique identifier for each customer.
- **Name**: Name of the customer.
- **Email**: Contact email of the customer.
- **Phone**: Contact phone number.

### Orders Table
- **OrderID**: Unique identifier for each order.
- **CustomerID**: Identifier linking the order to a customer.
- **OrderDate**: Date when the order was placed.

### MenuItemType Table
- **TypeID**: Unique identifier for each menu item type.
- **TypeName**: Name of the menu item type (e.g., Appetizer, Main Course).

### MenuItem Table
- **MenuItemID**: Unique identifier for each menu item.
- **TypeID**: Identifier linking the menu item to a type.
- **Name**: Name of the menu item.
- **Price**: Price of the menu item.

### OrderDetail Table
- **OrderDetailID**: Unique identifier for each order detail.
- **OrderID**: Identifier linking the order detail to an order.
- **MenuItemID**: Identifier linking the order detail to a menu item.
- **Quantity**: Quantity of the menu item ordered.

### Payment Table
- **PaymentID**: Unique identifier for each payment.
- **OrderID**: Identifier linking the payment to an order.
- **PaymentAmount**: Amount of the payment.
- **PaymentDate**: Date when the payment was made.
- **PaymentMethod**: Method of payment (e.g., Cash, Credit Card).

### Rating Table
- **RatingID**: Unique identifier for each rating.
- **MenuItemID**: Identifier linking the rating to a menu item.
- **CustomerID**: Identifier linking the rating to a customer.
- **RatingValue**: Rating value (e.g., 1 to 5 stars).
- **Review**: Text review of the menu item.

## Credits

### Team Members
- Abubakar
- Zunaira Akbar
- Danish Abdullah Khan

### Third-Party Libraries
- **Tkinter**: GUI library for Python.
- **MySQL Connector/Python**: Connector for MySQL databases in Python.

### ChatGPT for Help
- ChatGPT, an AI language Assistant, was used to assist with technical queries and guidance.
