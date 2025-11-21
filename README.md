🍽️ MealMate – Online Food Ordering System
![Uploading image.png…]()

MealMate is an intuitive and efficient online food ordering system designed to simplify the way customers browse menus, add items to their cart, and place orders. Built using Python Django, it ensures a smooth and secure ordering experience with real-time cart updates and Razorpay payment integration. The platform provides a clean user interface for customers and powerful management tools for admins. MealMate delivers convenience, speed, and reliability—bringing a complete food ordering solution to life.
🚀 Project Overview

MealMate is a full-stack online food ordering system that allows users to:

Browse restaurants & food menus

Add items to cart

Place orders

Make secure online payments (Razorpay)

Manage restaurants (Admin Panel)

This project is built using Django (Backend) and HTML, CSS, JavaScript (Frontend).

🛠️ Tech Stack
Frontend

HTML5

CSS3

JavaScript


Backend

Python

Django Framework

SQLite 

Payment Integration

Razorpay

📌 Features
👤 User Features

User Login / Signup

Browse restaurant menu

Add to cart

Increase/Decrease quantity

Online Payment

Order Confirmation Page


🛍️ Cart & Orders

Dynamic cart update

Auto Total Price Calculation

Store order details

Order management for admin

🛠️ Admin Features

Add/Edit/Delete menu items

View all customer orders

Manage customers & restaurants

📂 Project Structure

MealMate/
│── delivery/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── static/
│
│── mealmate_project/
│── manage.py
│── requirements.txt
│── README.md

Installation & Setup
1. Clone the Repository
git clone https://github.com/your-username/mealmate.git
cd mealmate
2. Set Up a Virtual Environment
python3 -m venv venv
source venv/bin/activate  # For Mac/Linux
3. Install Dependencies
pip install -r requirements.txt
4. Apply Migrations
python manage.py migrate
5. Create a Superuser
python manage.py createsuperuser
6. Run the Development Server
python manage.py runserver
Now, open your browser and go to http://127.0.0.1:8000/

💳 Razorpay Setup

Add the following to your project settings or .env file:

RAZORPAY_KEY_ID=your_key_id
RAZORPAY_KEY_SECRET=your_key_secret

🍽️ API Endpoints – MealMate Project
📌 User & Authentication
Method	Endpoint	Description
POST	/auth/register/	Register a new user
POST	/auth/login/	User login
GET	/auth/profile/	Get user profile
📌 Restaurants
Method	Endpoint	Description
GET	/restaurants/	List all restaurants
POST	/restaurants/add/	Add a new restaurant
PUT	/restaurants/update/<id>/	Update restaurant details
DELETE	/restaurants/delete/<id>/	Delete a restaurant
📌 Menu
Method	Endpoint	Description
GET	/menu/	Get all menu items
GET	/menu/<id>/	Get a single menu item
POST	/menu/add/	Add menu item (Admin)
PUT	/menu/update/<id>/	Update menu item
DELETE	/menu/delete/<id>/	Delete menu item
📌 Cart
Method	Endpoint	Description
GET	/cart/<username>/	View user cart
POST	/cart/add/	Add item to cart
PUT	/cart/update/<item_id>/	Update quantity
DELETE	/cart/remove/<item_id>/	Remove item
DELETE	/cart/clear/<username>/	Clear full cart
