# 📚 Computer Science Book Store

One of my favorite Django projects that I started by myself! This is a work-in-progress and will continue to evolve as I learn and build more features.

---

## 🔧 Current Features

The site currently supports:

- 📦 Three main apps: `Blog`, `Users`, and `Store`
- 🔍 Full-text **search** across books, authors, and categories
- ✉️ **SMTP integration** for email-based features
- 👤 **User panel** includes:
  - Edit user info
  - Password reset
  - Password change
- 📰 **Blog system** with latest posts about programming languages, etc.
- 🎨 User-friendly HTML forms styled with CSS
- 🌐 **Persian (Farsi)** interface with RTL-friendly design
- 🔐 **Role-based access control** for users and admins

---

## 🌱 Planned Features (Coming Soon)

- 🛒 **Shopping cart** functionality
- 💳 **Checkout system** with order tracking and payments
- 🌐 **REST API** using Django REST Framework (DRF)
- 📱 **Responsive design** for mobile and tablets
- 🧠 More features as I continue to learn and improve!

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Database**: PostgreSQL
- **Frontend**: HTML5, CSS3 (RTL + Persian-compatible)
- **Image Handling**: Django `ImageField`
- **Authentication**: Overwritten Django built-in user system

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/AvaGhiasian/CS-Bookstore
cd CS-Bookstore
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---
👤 Author

Ava Ghiasian
Aspiring backend developer | Passionate about learning and building