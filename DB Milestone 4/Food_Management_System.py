import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Developer@123',
        database='Kamal_Restaurant'
    )

# Customer Management Functions
def insert_customer():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('InsertCustomer', (email_entry.get(), phone_entry.get(), address_entry.get()))
        conn.commit()
        messagebox.showinfo("Success", "Customer added successfully")
        display_customers()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to insert record into database: {error}")
    finally:
        cursor.close()
        conn.close()

def update_customer():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        customer_id = customer_id_entry.get()
        if customer_id == '':
            raise ValueError("Customer ID cannot be empty")
        cursor.callproc('UpdateCustomer', (int(customer_id), email_entry.get(), phone_entry.get(), address_entry.get()))
        conn.commit()
        messagebox.showinfo("Success", "Customer updated successfully")
        display_customers()
    except ValueError as error:
        messagebox.showerror("Error", str(error))
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to update record in database: {error}")
    finally:
        cursor.close()
        conn.close()

def delete_customer():
    customer_id = customer_id_entry.get()  # Get the value from the customer_id_entry widget
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('DeleteCustomer', (int(customer_id),))
        conn.commit()
        messagebox.showinfo("Success", "Customer deleted successfully")
        display_customers()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to delete record from database: {error}")
    finally:
        cursor.close()
        conn.close()

def search_customers():
    for row in customer_tree.get_children():
        customer_tree.delete(row)
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('SearchCustomersByEmail', (customer_search_entry.get(),))
        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
                customer_tree.insert("", tk.END, values=row)
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to search records in database: {error}")
    finally:
        cursor.close()
        conn.close()

def display_customers():
    for row in customer_tree.get_children():
        customer_tree.delete(row)
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Customer")
        rows = cursor.fetchall()
        for row in rows:
            customer_tree.insert("", tk.END, values=row)
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to retrieve records from database: {error}")
    finally:
        cursor.close()
        conn.close()

# Order Management Functions
def insert_order():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('InsertOrder', (int(order_customer_id_entry.get()), order_date_entry.get()))
        conn.commit()
        messagebox.showinfo("Success", "Order added successfully")
        display_orders()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to insert record into database: {error}")
    finally:
        cursor.close()
        conn.close()

def update_order():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('UpdateOrder', (int(order_id_entry.get()), int(order_customer_id_entry.get()), order_date_entry.get()))
        conn.commit()
        messagebox.showinfo("Success", "Order updated successfully")
        display_orders()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to update record in database: {error}")
    finally:
        cursor.close()
        conn.close()

def delete_order():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('DeleteOrder', (int(order_id_entry.get()),))
        conn.commit()
        messagebox.showinfo("Success", "Order deleted successfully")
        display_orders()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to delete record from database: {error}")
    finally:
        cursor.close()
        conn.close()

def search_orders():
    for row in order_tree.get_children():
        order_tree.delete(row)
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('SearchOrdersByCustomerID', (int(order_search_entry.get()),))
        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
                order_tree.insert("", tk.END, values=row)
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to search records in database: {error}")
    finally:
        cursor.close()
        conn.close()

def display_orders():
    for row in order_tree.get_children():
        order_tree.delete(row)
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Orders")
        rows = cursor.fetchall()
        for row in rows:
            order_tree.insert("", tk.END, values=row)
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to retrieve records from database: {error}")
    finally:
        cursor.close()
        conn.close()

# Menu Item Type Management Functions
def insert_menu_item_type():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('InsertMenuItemType', (type_name_entry.get(),))
        conn.commit()
        messagebox.showinfo("Success", "Menu Item Type added successfully")
        display_menu_item_types()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to insert record into database: {error}")
    finally:
        cursor.close()
        conn.close()

def update_menu_item_type():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('UpdateMenuItemType', (int(type_id_entry.get()), type_name_entry.get()))
        conn.commit()
        messagebox.showinfo("Success", "Menu Item Type updated successfully")
        display_menu_item_types()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to update record in database: {error}")
    finally:
        cursor.close()
        conn.close()

def delete_menu_item_type():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('DeleteMenuItemType', (int(type_id_entry.get()),))
        conn.commit()
        messagebox.showinfo("Success", "Menu Item Type deleted successfully")
        display_menu_item_types()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to delete record from database: {error}")
    finally:
        cursor.close()
        conn.close()

def search_menu_item_types():
    for row in tree.get_children():
        tree.delete(row)
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('SearchMenuItemTypes')
        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row)
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to search records in database: {error}")
    finally:
        cursor.close()
        conn.close()

def display_menu_item_types():
    for row in tree.get_children():
        tree.delete(row)
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM MenuItemType")
        rows = cursor.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to retrieve records from database: {error}")
    finally:
        cursor.close()
        conn.close()

# Menu Item Management Functions
def insert_menu_item():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('InsertMenuItem', (menu_name_entry.get(), price_entry.get(), description_entry.get(), int(type_id_entry.get())))
        conn.commit()
        messagebox.showinfo("Success", "Menu Item added successfully")
        display_menu_items()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to insert record into database: {error}")
    finally:
        cursor.close()
        conn.close()

def update_menu_item():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('UpdateMenuItem', (int(item_id_entry.get()), menu_name_entry.get(), price_entry.get(), description_entry.get(), int(type_id_entry.get())))
        conn.commit()
        messagebox.showinfo("Success", "Menu Item updated successfully")
        display_menu_items()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to update record in database: {error}")
    finally:
        cursor.close()
        conn.close()

def delete_menu_item():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('DeleteMenuItem', (int(item_id_entry.get()),))
        conn.commit()
        messagebox.showinfo("Success", "Menu Item deleted successfully")
        display_menu_items()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to delete record from database: {error}")
    finally:
        cursor.close()
        conn.close()

def search_menu_items_by_type():
    for row in tree.get_children():
        tree.delete(row)
    
    conn = create_connection()
    cursor = conn.cursor()
    
    try:
        cursor.callproc('SearchMenuItemsByMenuItemTypeID', (int(type_id_entry.get()),))
        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row)
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to search records in database: {error}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def display_menu_items():
    for row in tree.get_children():
        tree.delete(row)
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM MenuItem")
        rows = cursor.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to retrieve records from database: {error}")
    finally:
        cursor.close()
        conn.close()

# Order Details MAnagement
def insert_order_detail():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('InsertOrderDetail', (int(order_id_entry.get()), int(menu_item_id_entry.get()), int(quantity_entry.get()), special_instructions_entry.get()))
        conn.commit()
        messagebox.showinfo("Success", "Order Detail added successfully")
        display_order_details()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to insert record into database: {error}")
    finally:
        cursor.close()
        conn.close()

def update_order_detail():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('UpdateOrderDetail', (int(order_detail_id_entry.get()), int(order_id_entry.get()), int(menu_item_id_entry.get()), int(quantity_entry.get()), special_instructions_entry.get()))
        conn.commit()
        messagebox.showinfo("Success", "Order Detail updated successfully")
        display_order_details()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to update record in database: {error}")
    finally:
        cursor.close()
        conn.close()

def delete_order_detail():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('DeleteOrderDetail', (int(order_detail_id_entry.get()),))
        conn.commit()
        messagebox.showinfo("Success", "Order Detail deleted successfully")
        display_order_details()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to delete record from database: {error}")
    finally:
        cursor.close()
        conn.close()

def search_order_details():
    for row in tree.get_children():
        tree.delete(row)
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('SearchOrderDetails', (int(order_id_entry.get()),))
        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row)
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to search records in database: {error}")
    finally:
        cursor.close()
        conn.close()

def display_order_details():
    for row in tree.get_children():
        tree.delete(row)
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM OrderDetail")
        rows = cursor.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to retrieve records from database: {error}")
    finally:
        cursor.close()
        conn.close()

# Payment Management 
def insert_payment():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('InsertPayment', (int(order_id_entry.get()), float(payment_amount_entry.get()), payment_date_entry.get(), payment_method_entry.get()))
        conn.commit()
        messagebox.showinfo("Success", "Payment added successfully")
        display_payments()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to insert record into database: {error}")
    finally:
        cursor.close()
        conn.close()

def update_payment():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('UpdatePayment', (int(payment_id_entry.get()), int(order_id_entry.get()), float(payment_amount_entry.get()), payment_date_entry.get(), payment_method_entry.get()))
        conn.commit()
        messagebox.showinfo("Success", "Payment updated successfully")
        display_payments()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to update record in database: {error}")
    finally:
        cursor.close()
        conn.close()

def delete_payment():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('DeletePayment', (int(payment_id_entry.get()),))
        conn.commit()
        messagebox.showinfo("Success", "Payment deleted successfully")
        display_payments()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to delete record from database: {error}")
    finally:
        cursor.close()
        conn.close()

def search_payments():
    for row in tree.get_children():
        tree.delete(row)
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('SearchPayments', (int(order_id_entry.get()),))
        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row)
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to search records in database: {error}")
    finally:
        cursor.close()
        conn.close()

def display_payments():
    for row in tree.get_children():
        tree.delete(row)
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Payment")
        rows = cursor.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to retrieve records from database: {error}")
    finally:
        cursor.close()
        conn.close()

# RAting Management
def insert_rating():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('InsertRating', (int(menu_item_id_entry.get()), int(rating_value_entry.get()), review_entry.get(), int(customer_id_entry.get())))
        conn.commit()
        messagebox.showinfo("Success", "Rating added successfully")
        display_ratings()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to insert record into database: {error}")
    finally:
        cursor.close()
        conn.close()

def update_rating():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('UpdateRating', (int(rating_id_entry.get()), int(menu_item_id_entry.get()), int(rating_value_entry.get()), review_entry.get(), int(customer_id_entry.get())))
        conn.commit()
        messagebox.showinfo("Success", "Rating updated successfully")
        display_ratings()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to update record in database: {error}")
    finally:
        cursor.close()
        conn.close()

def delete_rating():
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('DeleteRating', (int(rating_id_entry.get()),))
        conn.commit()
        messagebox.showinfo("Success", "Rating deleted successfully")
        display_ratings()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to delete record from database: {error}")
    finally:
        cursor.close()
        conn.close()

def search_ratings():
    for row in tree.get_children():
        tree.delete(row)
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.callproc('SearchRatings', (int(menu_item_id_entry.get()),))
        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row)
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to search records in database: {error}")
    finally:
        cursor.close()
        conn.close()

def display_ratings():
    for row in tree.get_children():
        tree.delete(row)
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Rating")
        rows = cursor.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to retrieve records from database: {error}")
    finally:
        cursor.close()
        conn.close()

def on_button_enter(e):
    e.widget['background'] = '#3E8E41'

def on_button_leave(e):
    e.widget['background'] = '#4CAF50'

app = tk.Tk()
app.title("Food Management System")
app.geometry("800x600")
app.configure(bg='#F0F0F0')

style = ttk.Style()
style.configure("Treeview.Heading", font=('Helvetica', 10, 'bold'))

notebook = ttk.Notebook(app)
notebook.pack(pady=10, expand=True)

customer_frame = tk.Frame(notebook, bg='#F0F0F0')
order_frame = tk.Frame(notebook, bg='#F0F0F0')
menuitemtype_frame = tk.Frame(notebook, bg='#F0F0F0')
app_menu_item = tk.Frame(notebook, bg='#F0F0F0')
app_order_detail = tk.Frame(notebook, bg='#F0F0F0')
app_payment = tk.Frame(notebook, bg='#F0F0F0')
app_rating = tk.Frame(notebook, bg='#F0F0F0')

notebook.add(customer_frame, text="Customer Management")
notebook.add(order_frame, text="Order Management")
notebook.add(menuitemtype_frame, text="MenuItemType Management")
notebook.add(app_menu_item, text="Menu Item Management")
notebook.add(app_order_detail, text="Order Detail Management")
notebook.add(app_payment, text="Payment Management")
notebook.add(app_rating, text="Rating Management")

# Customer Management UI
customer_title_label = tk.Label(customer_frame, text="Customer Management System", font=("Helvetica", 16), bg='#F0F0F0')
customer_title_label.grid(row=0, column=0, columnspan=3, pady=10)

customer_form_frame = tk.Frame(customer_frame, bg='#F0F0F0')
customer_form_frame.grid(row=1, column=0, columnspan=3, padx=20, pady=10)

tk.Label(customer_form_frame, text="Customer ID", bg='#F0F0F0').grid(row=0, column=0)
customer_id_entry = tk.Entry(customer_form_frame)
customer_id_entry.grid(row=0, column=1)

tk.Label(customer_form_frame, text="Email", bg='#F0F0F0').grid(row=1, column=0)
email_entry = tk.Entry(customer_form_frame)
email_entry.grid(row=1, column=1)

tk.Label(customer_form_frame, text="Phone", bg='#F0F0F0').grid(row=2, column=0)
phone_entry = tk.Entry(customer_form_frame)
phone_entry.grid(row=2, column=1)

tk.Label(customer_form_frame, text="Address", bg='#F0F0F0').grid(row=3, column=0)
address_entry = tk.Entry(customer_form_frame)
address_entry.grid(row=3, column=1)

customer_button_frame = tk.Frame(customer_frame, bg='#F0F0F0')
customer_button_frame.grid(row=2, column=0, columnspan=3, pady=10)

add_customer_button = tk.Button(customer_button_frame, text="Add Customer", command=insert_customer, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
add_customer_button.grid(row=0, column=0, padx=5)
add_customer_button.bind("<Enter>", on_button_enter)
add_customer_button.bind("<Leave>", on_button_leave)

update_customer_button = tk.Button(customer_button_frame, text="Update Customer", command=update_customer, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
update_customer_button.grid(row=0, column=1, padx=5)
update_customer_button.bind("<Enter>", on_button_enter)
update_customer_button.bind("<Leave>", on_button_leave)

delete_customer_button = tk.Button(customer_button_frame, text="Delete Customer", command=delete_customer, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
delete_customer_button.grid(row=0, column=2, padx=5)
delete_customer_button.bind("<Enter>", on_button_enter)
delete_customer_button.bind("<Leave>", on_button_leave)

tk.Label(customer_frame, text="Search by Email", bg='#F0F0F0').grid(row=3, column=0)
customer_search_entry = tk.Entry(customer_frame)
customer_search_entry.grid(row=3, column=1)
search_customer_button = tk.Button(customer_frame, text="Search", command=search_customers, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
search_customer_button.grid(row=3, column=2)
search_customer_button.bind("<Enter>", on_button_enter)
search_customer_button.bind("<Leave>", on_button_leave)

customer_tree_frame = tk.Frame(customer_frame, bg='#F0F0F0')
customer_tree_frame.grid(row=4, column=0, columnspan=3, padx=20, pady=10)

customer_tree = ttk.Treeview(customer_tree_frame, columns=("CustomerID", "Email", "Phone", "Address"), show='headings', height=8)
customer_tree.heading("CustomerID", text="Customer ID")
customer_tree.heading("Email", text="Email")
customer_tree.heading("Phone", text="Phone")
customer_tree.heading("Address", text="Address")
customer_tree.pack(side='left')

customer_scrollbar = ttk.Scrollbar(customer_tree_frame, orient="vertical", command=customer_tree.yview)
customer_scrollbar.pack(side='right', fill='y')
customer_tree.configure(yscroll=customer_scrollbar.set)

display_customers()

# Order Management UI
order_title_label = tk.Label(order_frame, text="Order Management System", font=("Helvetica", 16), bg='#F0F0F0')
order_title_label.grid(row=0, column=0, columnspan=3, pady=10)

order_form_frame = tk.Frame(order_frame, bg='#F0F0F0')
order_form_frame.grid(row=1, column=0, columnspan=3, padx=20, pady=10)

tk.Label(order_form_frame, text="Order ID", bg='#F0F0F0').grid(row=0, column=0)
order_id_entry = tk.Entry(order_form_frame)
order_id_entry.grid(row=0, column=1)

tk.Label(order_form_frame, text="Customer ID", bg='#F0F0F0').grid(row=1, column=0)
order_customer_id_entry = tk.Entry(order_form_frame)
order_customer_id_entry.grid(row=1, column=1)

tk.Label(order_form_frame, text="Order Date", bg='#F0F0F0').grid(row=2, column=0)
order_date_entry = tk.Entry(order_form_frame)
order_date_entry.grid(row=2, column=1)

order_button_frame = tk.Frame(order_frame, bg='#F0F0F0')
order_button_frame.grid(row=2, column=0, columnspan=3, pady=10)

add_order_button = tk.Button(order_button_frame, text="Add Order", command=insert_order, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
add_order_button.grid(row=0, column=0, padx=5)
add_order_button.bind("<Enter>", on_button_enter)
add_order_button.bind("<Leave>", on_button_leave)

update_order_button = tk.Button(order_button_frame, text="Update Order", command=update_order, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
update_order_button.grid(row=0, column=1, padx=5)
update_order_button.bind("<Enter>", on_button_enter)
update_order_button.bind("<Leave>", on_button_leave)

delete_order_button = tk.Button(order_button_frame, text="Delete Order", command=delete_order, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
delete_order_button.grid(row=0, column=2, padx=5)
delete_order_button.bind("<Enter>", on_button_enter)
delete_order_button.bind("<Leave>", on_button_leave)

tk.Label(order_frame, text="Search by Customer ID", bg='#F0F0F0').grid(row=3, column=0)
order_search_entry = tk.Entry(order_frame)
order_search_entry.grid(row=3, column=1)
search_order_button = tk.Button(order_frame, text="Search", command=search_orders, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
search_order_button.grid(row=3, column=2)
search_order_button.bind("<Enter>", on_button_enter)
search_order_button.bind("<Leave>", on_button_leave)

order_tree_frame = tk.Frame(order_frame, bg='#F0F0F0')
order_tree_frame.grid(row=4, column=0, columnspan=3, padx=20, pady=10)

order_tree = ttk.Treeview(order_tree_frame, columns=("OrderID", "CustomerID", "OrderDate"), show='headings', height=8)
order_tree.heading("OrderID", text="Order ID")
order_tree.heading("CustomerID", text="Customer ID")
order_tree.heading("OrderDate", text="Order Date")
order_tree.pack(side='left')

order_scrollbar = ttk.Scrollbar(order_tree_frame, orient="vertical", command=order_tree.yview)
order_scrollbar.pack(side='right', fill='y')
order_tree.configure(yscroll=order_scrollbar.set)

display_orders()

#MeniItemTpe MAnagement UI
# Menu Item Type Management UI
title_label = tk.Label(menuitemtype_frame, text="Menu Item Type Management System", font=("Helvetica", 16), bg='#F0F0F0')
title_label.grid(row=0, column=0, columnspan=3, pady=10)

form_frame = tk.Frame(menuitemtype_frame, bg='#F0F0F0')
form_frame.grid(row=1, column=0, columnspan=3, padx=20, pady=10)

tk.Label(form_frame, text="Type ID", bg='#F0F0F0').grid(row=0, column=0)
type_id_entry = tk.Entry(form_frame)
type_id_entry.grid(row=0, column=1)

tk.Label(form_frame, text="Type Name", bg='#F0F0F0').grid(row=1, column=0)
type_name_entry = tk.Entry(form_frame)
type_name_entry.grid(row=1, column=1)

button_frame = tk.Frame(menuitemtype_frame, bg='#F0F0F0')
button_frame.grid(row=2, column=0, columnspan=3, pady=10)

add_button = tk.Button(button_frame, text="Add Menu Item Type", command=insert_menu_item_type, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
add_button.grid(row=0, column=0, padx=5)

update_button = tk.Button(button_frame, text="Update Menu Item Type", command=update_menu_item_type, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
update_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Delete Menu Item Type", command=delete_menu_item_type, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
delete_button.grid(row=0, column=2, padx=5)

tk.Label(menuitemtype_frame, text="Search by Type Name", bg='#F0F0F0').grid(row=3, column=0)
menu_type_search_entry = tk.Entry(menuitemtype_frame)
menu_type_search_entry.grid(row=3, column=1)

search_menu_type_button = tk.Button(menuitemtype_frame, text="Search", command=search_menu_item_types, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
search_menu_type_button.grid(row=3, column=2)
search_menu_type_button.bind("<Enter>", on_button_enter)
search_menu_type_button.bind("<Leave>", on_button_leave)

tree_frame = tk.Frame(menuitemtype_frame, bg='#F0F0F0')
tree_frame.grid(row=4, column=0, columnspan=3, padx=20, pady=10)

tree = ttk.Treeview(tree_frame, columns=("MenuItemTypeID", "TypeName"), show='headings', height=8)
tree.heading("MenuItemTypeID", text="Menu Item Type ID")
tree.heading("TypeName", text="Type Name")
tree.pack(side='left')

scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
scrollbar.pack(side='right', fill='y')
tree.configure(yscroll=scrollbar.set)

display_menu_item_types()

#Menu Item Management UI
title_label = tk.Label(app_menu_item, text="Menu Item Management System", font=("Helvetica", 16), bg='#F0F0F0')
title_label.grid(row=0, column=0, columnspan=3, pady=10)

form_frame = tk.Frame(app_menu_item, bg='#F0F0F0')
form_frame.grid(row=1, column=0, columnspan=3, padx=20, pady=10)

tk.Label(form_frame, text="Item ID", bg='#F0F0F0').grid(row=0, column=0)
item_id_entry = tk.Entry(form_frame)
item_id_entry.grid(row=0, column=1)

tk.Label(form_frame, text="Menu Name", bg='#F0F0F0').grid(row=1, column=0)
menu_name_entry = tk.Entry(form_frame)
menu_name_entry.grid(row=1, column=1)

tk.Label(form_frame, text="Price", bg='#F0F0F0').grid(row=2, column=0)
price_entry = tk.Entry(form_frame)
price_entry.grid(row=2, column=1)

tk.Label(form_frame, text="Description", bg='#F0F0F0').grid(row=3, column=0)
description_entry = tk.Entry(form_frame)
description_entry.grid(row=3, column=1)

tk.Label(form_frame, text="Type ID", bg='#F0F0F0').grid(row=4, column=0)
type_id_entry = tk.Entry(form_frame)
type_id_entry.grid(row=4, column=1)

button_frame = tk.Frame(app_menu_item, bg='#F0F0F0')
button_frame.grid(row=2, column=0, columnspan=3, pady=10)

add_button = tk.Button(button_frame, text="Add Menu Item", command=insert_menu_item, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
add_button.grid(row=0, column=0, padx=5)

update_button = tk.Button(button_frame, text="Update Menu Item", command=update_menu_item, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
update_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Delete Menu Item", command=delete_menu_item, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
delete_button.grid(row=0, column=2, padx=5)

tk.Label(app_menu_item, text="Search by Menu Name", bg='#F0F0F0').grid(row=3, column=0)
menu_item_search_entry = tk.Entry(app_menu_item)
menu_item_search_entry.grid(row=3, column=1)
search_menu_item_button = tk.Button(app_menu_item, text="Search", command=search_menu_items_by_type, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
search_menu_item_button.grid(row=3, column=2)
search_menu_item_button.bind("<Enter>", on_button_enter)
search_menu_item_button.bind("<Leave>", on_button_leave)

tree_frame = tk.Frame(app_menu_item, bg='#F0F0F0')
tree_frame.grid(row=4, column=0, columnspan=3, padx=20, pady=10)

tree = ttk.Treeview(tree_frame, columns=("MenuItemID", "MenuName", "Price", "Description", "MenuItemTypeID"), show='headings', height=8)
tree.heading("MenuItemID", text="Menu Item ID")
tree.heading("MenuName", text="Menu Name")
tree.heading("Price", text="Price")
tree.heading("Description", text="Description")
tree.heading("MenuItemTypeID", text="Type ID")
tree.pack(side='left')

scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
scrollbar.pack(side='right', fill='y')
tree.configure(yscroll=scrollbar.set)

display_menu_items()

#Order Detail Management UI
title_label = tk.Label(app_order_detail, text="Order Detail Management System", font=("Helvetica", 16), bg='#F0F0F0')
title_label.grid(row=0, column=0, columnspan=4, pady=10)

form_frame = tk.Frame(app_order_detail, bg='#F0F0F0')
form_frame.grid(row=1, column=0, columnspan=4, padx=20, pady=10)

tk.Label(form_frame, text="Order Detail ID", bg='#F0F0F0').grid(row=0, column=0)
order_detail_id_entry = tk.Entry(form_frame)
order_detail_id_entry.grid(row=0, column=1)

tk.Label(form_frame, text="Order ID", bg='#F0F0F0').grid(row=1, column=0)
order_id_entry = tk.Entry(form_frame)
order_id_entry.grid(row=1, column=1)

tk.Label(form_frame, text="Menu Item ID", bg='#F0F0F0').grid(row=2, column=0)
menu_item_id_entry = tk.Entry(form_frame)
menu_item_id_entry.grid(row=2, column=1)

tk.Label(form_frame, text="Quantity", bg='#F0F0F0').grid(row=3, column=0)
quantity_entry = tk.Entry(form_frame)
quantity_entry.grid(row=3, column=1)

tk.Label(form_frame, text="Special Instructions", bg='#F0F0F0').grid(row=4, column=0)
special_instructions_entry = tk.Entry(form_frame)
special_instructions_entry.grid(row=4, column=1)

button_frame = tk.Frame(app_order_detail, bg='#F0F0F0')
button_frame.grid(row=2, column=0, columnspan=4, pady=10)

add_button = tk.Button(button_frame, text="Add Order Detail", command=insert_order_detail, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
add_button.grid(row=0, column=0, padx=5)

update_button = tk.Button(button_frame, text="Update Order Detail", command=update_order_detail, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
update_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Delete Order Detail", command=delete_order_detail, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
delete_button.grid(row=0, column=2, padx=5)

tk.Label(app_order_detail, text="Search by Order ID", bg='#F0F0F0').grid(row=3, column=0)
order_detail_search_entry = tk.Entry(app_order_detail)
order_detail_search_entry.grid(row=3, column=1)
search_order_detail_button = tk.Button(app_order_detail, text="Search", command=search_order_details, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
search_order_detail_button.grid(row=3, column=2)
search_order_detail_button.bind("<Enter>", on_button_enter)
search_order_detail_button.bind("<Leave>", on_button_leave)

tree_frame = tk.Frame(app_order_detail, bg='#F0F0F0')
tree_frame.grid(row=4, column=0, columnspan=4, padx=20, pady=10)

tree = ttk.Treeview(tree_frame, columns=("OrderDetailID", "OrderID", "MenuItemID", "Quantity", "SpecialInstructions"), show='headings', height=8)
tree.heading("OrderDetailID", text="Order Detail ID")
tree.heading("OrderID", text="Order ID")
tree.heading("MenuItemID", text="Menu Item ID")
tree.heading("Quantity", text="Quantity")
tree.heading("SpecialInstructions", text="Special Instructions")
tree.pack(side='left')

scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
scrollbar.pack(side='right', fill='y')
tree.configure(yscroll=scrollbar.set)

display_order_details()

#Payment Management UI
title_label = tk.Label(app_payment, text="Payment Management System", font=("Helvetica", 16), bg='#F0F0F0')
title_label.grid(row=0, column=0, columnspan=3, pady=10)

form_frame = tk.Frame(app_payment, bg='#F0F0F0')
form_frame.grid(row=1, column=0, columnspan=3, padx=20, pady=10)

tk.Label(form_frame, text="Payment ID", bg='#F0F0F0').grid(row=0, column=0)
payment_id_entry = tk.Entry(form_frame)
payment_id_entry.grid(row=0, column=1)

tk.Label(form_frame, text="Order ID", bg='#F0F0F0').grid(row=1, column=0)
order_id_entry = tk.Entry(form_frame)
order_id_entry.grid(row=1, column=1)

tk.Label(form_frame, text="Payment Amount", bg='#F0F0F0').grid(row=2, column=0)
payment_amount_entry = tk.Entry(form_frame)
payment_amount_entry.grid(row=2, column=1)

tk.Label(form_frame, text="Payment Date", bg='#F0F0F0').grid(row=3, column=0)
payment_date_entry = tk.Entry(form_frame)
payment_date_entry.grid(row=3, column=1)

tk.Label(form_frame, text="Payment Method", bg='#F0F0F0').grid(row=3, column=0)
payment_method_entry = ttk.Combobox(form_frame, values=["Cash", "Credit Card", "Debit Card"])
payment_method_entry.grid(row=3, column=1)

button_frame = tk.Frame(app_payment, bg='#F0F0F0')
button_frame.grid(row=2, column=0, columnspan=3, pady=10)

add_button = tk.Button(button_frame, text="Add Payment", command=insert_payment, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
add_button.grid(row=0, column=0, padx=5)

update_button = tk.Button(button_frame, text="Update Payment", command=update_payment, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
update_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Delete Payment", command=delete_payment, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
delete_button.grid(row=0, column=2, padx=5)

tk.Label(app_payment, text="Search by Order ID", bg='#F0F0F0').grid(row=3, column=0)
payment_search_entry = tk.Entry(app_payment)
payment_search_entry.grid(row=3, column=1)
search_payment_button = tk.Button(app_payment, text="Search", command=search_payments, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
search_payment_button.grid(row=3, column=2)
search_payment_button.bind("<Enter>", on_button_enter)
search_payment_button.bind("<Leave>", on_button_leave)

tree_frame = tk.Frame(app_payment, bg='#F0F0F0')
tree_frame.grid(row=4, column=0, columnspan=3, padx=20, pady=10)

tree = ttk.Treeview(tree_frame, columns=("PaymentID", "OrderID", "PaymentAmount", "PaymentDate", "PaymentMethod"), show='headings', height=8)
tree.heading("PaymentID", text="Payment ID")
tree.heading("OrderID", text="Order ID")
tree.heading("PaymentAmount", text="Payment Amount")
tree.heading("PaymentDate", text="Payment Date")
tree.heading("PaymentMethod", text="Payment Method")
tree.pack(side='left')

scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
scrollbar.pack(side='right', fill='y')
tree.configure(yscroll=scrollbar.set)

display_payments()

#Rating Management UI
title_label = tk.Label(app_rating, text="Rating Management System", font=("Helvetica", 16), bg='#F0F0F0')
title_label.grid(row=0, column=0, columnspan=3, pady=10)

form_frame = tk.Frame(app_rating, bg='#F0F0F0')
form_frame.grid(row=1, column=0, columnspan=3, padx=20, pady=10)

tk.Label(form_frame, text="Rating ID", bg='#F0F0F0').grid(row=0, column=0)
rating_id_entry = tk.Entry(form_frame)
rating_id_entry.grid(row=0, column=1)

tk.Label(form_frame, text="Menu Item ID", bg='#F0F0F0').grid(row=1, column=0)
menu_item_id_entry = tk.Entry(form_frame)
menu_item_id_entry.grid(row=1, column=1)

tk.Label(form_frame, text="Rating Value", bg='#F0F0F0').grid(row=2, column=0)
rating_value_entry = tk.Entry(form_frame)
rating_value_entry.grid(row=2, column=1)

tk.Label(form_frame, text="Review", bg='#F0F0F0').grid(row=3, column=0)
review_entry = tk.Entry(form_frame)
review_entry.grid(row=3, column=1)

tk.Label(form_frame, text="Customer ID", bg='#F0F0F0').grid(row=4, column=0)
customer_id_entry = tk.Entry(form_frame)
customer_id_entry.grid(row=4, column=1)

button_frame = tk.Frame(app_rating, bg='#F0F0F0')
button_frame.grid(row=2, column=0, columnspan=3, pady=10)

add_button = tk.Button(button_frame, text="Add Rating", command=insert_rating, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
add_button.grid(row=0, column=0, padx=5)

update_button = tk.Button(button_frame, text="Update Rating", command=update_rating, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
update_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Delete Rating", command=delete_rating, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
delete_button.grid(row=0, column=2, padx=5)

tk.Label(app_rating, text="Search by Menu Item ID", bg='#F0F0F0').grid(row=3, column=0)
rating_search_entry = tk.Entry(app_rating)
rating_search_entry.grid(row=3, column=1)
search_rating_button = tk.Button(app_rating, text="Search", command=search_ratings, bg='#4CAF50', fg='white', font=('Helvetica', 10, 'bold'))
search_rating_button.grid(row=3, column=2)
search_rating_button.bind("<Enter>", on_button_enter)
search_rating_button.bind("<Leave>", on_button_leave)

tree_frame = tk.Frame(app_rating, bg='#F0F0F0')
tree_frame.grid(row=4, column=0, columnspan=3, padx=20, pady=10)

tree = ttk.Treeview(tree_frame, columns=("RatingID", "MenuItemID", "RatingValue", "Review", "CustomerID"), show='headings', height=8)
tree.heading("RatingID", text="Rating ID")
tree.heading("MenuItemID", text="Menu Item ID")
tree.heading("RatingValue", text="Rating Value")
tree.heading("Review", text="Review")
tree.heading("CustomerID", text="Customer ID")
tree.pack(side='left')

scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
scrollbar.pack(side='right', fill='y')
tree.configure(yscroll=scrollbar.set)

display_ratings()

app.mainloop()
