
                                           <h1 align="center" style="font-size:40px;"><b>🍽️ MealMate – Online Food Ordering System</b></h1>


<img width="1913" height="915" alt="Screenshot 2025-11-21 175205" src="https://github.com/user-attachments/assets/d911056f-e8b5-4eb2-8ec8-1f95ccb626e1" />

MealMate is a smart and intuitive online food ordering platform built using **Python Django**, offering seamless restaurant browsing, menu exploration, cart management, and secure online payments through **Razorpay**.
Designed with a clean UI and smooth workflows, MealMate delivers speed, convenience, and reliability for both customers and admins—bringing a complete food-ordering ecosystem to life.

---

## 🚀 **Project Overview**

MealMate allows users to:

✔ Browse nearby restaurants & menus
✔ Add/remove items from the cart
✔ Increase/decrease item quantities
✔ Place secure online orders
✔ Make payments via Razorpay
✔ Track and store order history
✔ Admin-side menu & restaurant management

This project combines a robust **Django backend** with a responsive **HTML, CSS, JS** frontend.

---

## 🛠️ **Tech Stack**

### **🔹 Frontend**

* HTML5
* CSS3
* JavaScript

### **🔹 Backend**

* Python
* Django Framework
* SQLite Database

### **🔹 Payment Gateway**

* Razorpay

---

## 📌 **Features**

### 👤 **User Features**

* Login & Signup
* Browse restaurant menus
* Add items to cart
* Modify item quantities
* Online payments
* Order confirmation page

### 🛍️ **Cart & Orders**

* Auto-updating cart
* Dynamic total price calculation
* Order storage in database
* Admin-side order overview

### 🛠️ **Admin Features**

* Add / Edit / Delete menu items
* Manage restaurants
* View all customer orders

---

## 📂 **Project Structure**

```
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
```

---

## ⚙️ **Installation & Setup**

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/your-username/mealmate.git
cd mealmate
```

### **2️⃣ Set Up Virtual Environment**

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4️⃣ Apply Migrations**

```bash
python manage.py migrate
```

### **5️⃣ Create Superuser**

```bash
python manage.py createsuperuser
```

### **6️⃣ Run the Server**

```bash
python manage.py runserver
```

Open: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** 🎉

---

## 💳 **Razorpay Setup**

Add this to your **.env** or **settings.py**:

```
RAZORPAY_KEY_ID=your_key_id
RAZORPAY_KEY_SECRET=your_key_secret
```

---

# 🍽️ **API Endpoints – MealMate**

## 🔐 **User & Authentication**

| Method | Endpoint          | Description         |
| ------ | ----------------- | ------------------- |
| POST   | `/auth/register/` | Register a new user |
| POST   | `/auth/login/`    | User login          |
| GET    | `/auth/profile/`  | Get user profile    |

---

## 🏪 **Restaurants**

| Method | Endpoint                    | Description               |
| ------ | --------------------------- | ------------------------- |
| GET    | `/restaurants/`             | List all restaurants      |
| POST   | `/restaurants/add/`         | Add a new restaurant      |
| PUT    | `/restaurants/update/<id>/` | Update restaurant details |
| DELETE | `/restaurants/delete/<id>/` | Delete a restaurant       |

---

## 🍲 **Menu**

| Method | Endpoint             | Description           |
| ------ | -------------------- | --------------------- |
| GET    | `/menu/`             | Get all menu items    |
| GET    | `/menu/<id>/`        | Get single menu item  |
| POST   | `/menu/add/`         | Add menu item (Admin) |
| PUT    | `/menu/update/<id>/` | Update menu item      |
| DELETE | `/menu/delete/<id>/` | Delete menu item      |

---

## 🛒 **Cart**

| Method | Endpoint                  | Description           |
| ------ | ------------------------- | --------------------- |
| GET    | `/cart/<username>/`       | View user cart        |
| POST   | `/cart/add/`              | Add item to cart      |
| PUT    | `/cart/update/<item_id>/` | Update item quantity  |
| DELETE | `/cart/remove/<item_id>/` | Remove item from cart |
| DELETE | `/cart/clear/<username>/` | Clear entire cart     |

---

## 📦 **Orders**

| Method | Endpoint               | Description              |
| ------ | ---------------------- | ------------------------ |
| POST   | `/order/create/`       | Create a new order       |
| GET    | `/order/<username>/`   | Get user orders          |
| GET    | `/orders/list/`        | Admin – list all orders  |
| GET    | `/order/details/<id>/` | Get single order details |


