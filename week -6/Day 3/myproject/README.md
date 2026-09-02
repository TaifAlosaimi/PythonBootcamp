
# 📚 Library

A Django web application for managing and displaying library book information.

## 📌 About the Project

This project was built using Django as part of the Python Web Development Bootcamp.


## 🚀 Features

- Display a list of books.
- View details for a specific book.
- Use Django views to handle requests.
- Use URL routing to connect URLs with views.
- Use Django templates to display content.
- Organize the project using a Django app.

## 🛠️ Technologies Used

- Python
- Django
- HTML
- Django Templates
- SQLite

## 📂 Project Structure

```text
myproject/
├── mysite/
│   ├── library/
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   └── library/
│   │   │       ├── base.html
│   │   │       ├── list.html
│   │   │       └── detail.html
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── mysite/
│   │   ├── settings.py
│   │   └── urls.py
│   │
│   ├── db.sqlite3
│   └── manage.py
│
└── venv/