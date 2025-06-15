# user-authentication


# Django Custom User Management App

This Django project is a user management system featuring custom user registration, login with error handling, profile picture upload, a dashboard, and an admin panel with extended functionality.

---

## 📁 Features

- Custom user model (`CustomUser`) extending `AbstractUser`
- User registration with profile picture upload
- Login with custom error messages for incorrect username/password
- Dashboard view for logged-in users
- View list of all registered users (admin-level view)
- Custom admin interface for managing users
- Fully functional Django Admin panel
- Crispy Forms integration for clean form rendering

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/shivam-1208/user-authentication.git
cd your-repo-name
```

### 2. Create virtual environment & activate it

```bash
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (for admin access)

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Visit the following URLs:

- Admin Panel: http://127.0.0.1:8000/admin/
- Login: http://127.0.0.1:8000/login/
- Signup: http://127.0.0.1:8000/signup/
- Dashboard: http://127.0.0.1:8000/dashboard/

---

## 🧩 Project Structure

```
task1_project/
├── task1_app/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│       ├── login.html
│       ├── signup.html
│       ├── dashboard.html
│       └── all_users.html
├── task1_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/uploads/
├── db.sqlite3
└── manage.py
```

---

