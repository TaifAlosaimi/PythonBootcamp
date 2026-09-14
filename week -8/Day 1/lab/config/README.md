# Feedback Form — Django

A modern and responsive feedback form built with Django.

This project demonstrates how to build and handle a Django form, validate user input, protect POST requests with CSRF, and redirect users after a successful submission.

---

## 📸 Screenshots

### Feedback Form
![Feedback Form](config/static/images/1.png.png)

### Form Fields
![Form Fields](config/static/images/2.png.png)

### Validation Error
![Validation Error](config/static/images/3.png.png)

### Successful Submission
![Successful Submission](config/static/images/4.png.png)

### Thank You Page
![Thank You Page](config/static/images/5.png.png)


---


## ✨ Features

- Django feedback form
- Name, email, message, and optional rating fields
- Email validation using Django's `EmailField`
- Custom message validation
- Message must contain at least 20 characters
- CSRF protection
- Visible validation errors
- Separate thank-you page after successful submission
- Responsive and modern UI
- Custom CSS styling

---

## 🛠️ Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite
- Git & GitHub

---

## 📁 Project Structure

```text
lab/
│
├── config/
│   ├── config/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── ...
│   │
│   ├── feedback/
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   └── feedback/
│   │   │       ├── contact.html
│   │   │       └── thank_you.html
│   │   ├── forms.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── ...
│   │
│   ├── static/
│   │   ├── css/
│   │   └── images/
│   │       ├── 1.png.png
│   │       ├── 2.png.png
│   │       ├── 3.png.png
│   │       ├── 4.png.png
│   │       └── 5.png.png
│   │
│   ├── manage.py
│   └── requirements.txt
│
└── README.md