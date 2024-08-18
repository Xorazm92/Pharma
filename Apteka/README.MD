# Capsule Pharmacy Management System

## Overview

Capsule Pharmacy Management System is a comprehensive application designed to manage pharmacy operations. It includes functionalities for both administrators and users, providing a seamless experience for managing inventory, sales, and customer interactions.

## Features

### Admin Panel
- User management (add, edit, delete users)
- Inventory management (add, edit, delete products)
- Supplier management
- Sales and payment tracking
- Category management
- Purchase and payment tracking

### User Panel
- Browse and search products
- Add items to cart
- View special offers
- Place orders
- View order history
- User profile management

## Technical Stack

- **Backend**: Python with MySQL database
- **Frontend**: PyQt6 for GUI
- **Database**: MySQL

## Project Structure

1. `back.py`: Contains the Database class for handling all database operations.
2. `front.py`: Implements the GUI using PyQt6, including pages for admin and user interfaces.
3. `MySql_queries.sql`: SQL script for creating and initializing the database.

## Setup and Installation

1. Ensure you have Python installed (preferably Python 3.8+).
2. Install required packages:



3. Set up MySQL database:
- Create a database named `Apteka`
- Run the queries in `MySql_queries.sql` to set up tables and initial data

## Running the Application

1. Run `front.py` to start the application:

2. The application will open with a login screen. Use the following credentials:
- Admin: Login: "Lila", Password: "4681"
- User: Any other credentials from the Users table

## Key Components

### Database (`back.py`)
- Handles all database operations (CRUD)
- Manages connections to MySQL database
- Implements methods for user authentication, product management, and sales operations

### GUI (`front.py`)
- Implements the main application window
- Contains classes for different pages:
- `AboutPage`: Initial landing page
- `LoginPage`: User authentication
- `AdminPage`: Admin dashboard and operations
- `UserPage`: User interface for browsing and purchasing products

### Database Schema (`MySql_queries.sql`)
- Creates tables for Users, Suppliers, Customers, and Medics (products)
- Initializes the database with sample data

## Future Improvements

- Implement more robust error handling
- Add data visualization for sales and inventory
- Enhance security features (e.g., password hashing)
- Implement a logging system
- Add multi-language support

## Contributors

[List of contributors or your name]

## License

[Specify the license here]