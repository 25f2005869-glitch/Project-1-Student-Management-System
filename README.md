# 🎓 Student Management System

<p align="left">
  <img src="https://img.shields.io/badge/Project-Student%20Management%20System-blue" alt="Project">
  <img src="https://img.shields.io/badge/Framework-Flask-black" alt="Flask">
  <img src="https://img.shields.io/badge/Language-Python-blue" alt="Python">
  <img src="https://img.shields.io/badge/Database-SQLite-green" alt="SQLite">
  <img src="https://img.shields.io/badge/Course-Modern%20Application%20Development-orange" alt="MAD">
  <img src="https://img.shields.io/badge/IIT%20Madras-BS%20Degree-red" alt="IIT Madras">
  <img src="https://img.shields.io/badge/Level-Diploma-yellow" alt="Diploma">
  <img src="https://img.shields.io/badge/Status-In%20Progress-brightgreen" alt="Status">
</p>

---

## 👩‍💻 Author

**Saloni Tiwari**

**Programme:** IIT Madras BS Degree — Diploma Level  
**Course:** Modern Application Development I (MAD 1)  
**Project:** Project 1 — Student Management System  
**Technology:** Python + Flask  
**Database:** SQLite  
**Status:** In Progress

---

## 📌 About This Repository

This repository contains a Flask-based **Student Management System** developed as part of the **IIT Madras BS Degree — Diploma Level** learning journey.

The application provides a web-based platform for managing student records and implementing user authentication.

The project is being developed step-by-step with a focus on:

- 🐍 Python Web Development
- 🌐 Flask
- 🗄️ Database Management
- 🔐 Authentication
- 🔄 CRUD Operations
- 🧩 Modular Application Architecture
- 🐙 Git & GitHub

---

## 🎯 Project Objective

The main objective of this project is to build a practical web application using Flask while understanding the fundamentals of modern application development.

The project focuses on learning how different components of a web application work together:

- 🌐 Frontend
- ⚙️ Backend
- 🗄️ Database
- 🔐 Authentication
- 🧩 Application Architecture

---

## ✨ Features

### 👨‍🎓 Student Management

- ➕ Add Student
- 📋 View Students
- ✏️ Edit Student
- 🗑️ Delete Student
- 🔍 Search Student by Name
- 💾 SQLite Database Storage
- 🔢 Unique Roll Number
- 📧 Unique Email

### 🔐 Authentication

- 📝 User Registration
- 🔑 User Login
- 🚪 User Logout
- 🔒 Password Hashing
- 🔍 Password Verification
- 👤 Session Management
- 💬 Flash Messages
- ⚠️ Duplicate Username Detection
- ⚠️ Duplicate Email Detection

### 🎨 User Interface

- 🧭 Navigation Bar
- 📄 Reusable Base Template
- 📝 Student Forms
- 📊 Dashboard
- 💬 Flash Messages
- 🎨 Custom CSS Styling

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Programming Language |
| 🌐 Flask | Web Framework |
| 🗄️ Flask-SQLAlchemy | Database ORM |
| 🔐 Flask-Login | Authentication Support |
| 💾 SQLite | Database |
| 🧱 SQLAlchemy | Database Interaction |
| 🎨 HTML5 | Web Page Structure |
| 🎨 CSS3 | Styling |
| 🧩 Jinja2 | Template Engine |
| 🔒 Werkzeug | Password Hashing |
| 🐙 Git | Version Control |
| 🚀 GitHub | Repository Hosting |

---

## 📂 Project Structure

**Project 1 Student Management System/**

├── 📄 app.py  
├── ⚙️ config.py  
├── 🔌 extensions.py  
├── 📦 requirements.txt  
├── 📖 README.md  
├── 🚫 .gitignore  
│  
├── 🗄️ database/  
│   └── student.db  
│  
├── 🧩 models/  
│   ├── __init__.py  
│   ├── user.py  
│   └── student.py  
│  
├── 🛣️ routes/  
│   ├── auth.py  
│   └── student.py  
│  
├── 🎨 templates/  
│   ├── base.html  
│   ├── index.html  
│   ├── login.html  
│   ├── register.html  
│   ├── dashboard.html  
│   ├── add_student.html  
│   ├── students.html  
│   └── edit_student.html  
│  
├── 🎨 static/  
│   ├── css/  
│   │   └── style.css  
│   ├── js/  
│   │   └── script.js  
│   └── images/  
│  
└── 📸 screenshots/

---

## 🔄 Application Flow

### 👨‍🎓 Student Management

Request → Route → Model → SQLAlchemy → SQLite Database → Response → Template

### 🔐 Authentication

User → Register/Login → Authentication Route → User Model → Password Verification → Session → Dashboard

---

## 🗄️ Database Design

The application uses **SQLite** for data storage.

### 👨‍🎓 Student Table

| Field | Type | Description |
|---|---|---|
| `id` | Integer | Primary Key |
| `name` | String | Student Name |
| `roll_no` | String | Unique Roll Number |
| `department` | String | Department |
| `year` | Integer | Academic Year |
| `phone` | String | Phone Number |
| `email` | String | Student Email |
| `address` | Text | Student Address |

### 👤 User Table

| Field | Type | Description |
|---|---|---|
| `id` | Integer | Primary Key |
| `username` | String | Unique Username |
| `email` | String | Unique Email |
| `password_hash` | String | Hashed Password |

---

## 🔐 Password Security

Passwords are not stored as plain text.

The application uses **Werkzeug Security** for password hashing and password verification.

This provides a safer approach for storing user credentials.

---

## 🔄 CRUD Operations

| Operation | Feature | Status |
|---|---|---|
| 🟢 Create | Add Student | ✅ |
| 🔵 Read | View Students | ✅ |
| 🟡 Update | Edit Student | ✅ |
| 🔴 Delete | Delete Student | ✅ |
| 🔍 Search | Search by Name | ✅ |

---

## 🚀 Installation

### 1️⃣ Clone the Repository

git clone <YOUR-GITHUB-REPOSITORY-URL>

### 2️⃣ Open the Project

cd "Project 1 Student Management System"

### 3️⃣ Create Virtual Environment

python -m venv venv

### 4️⃣ Activate Virtual Environment

Windows PowerShell:

.\venv\Scripts\Activate.ps1

If PowerShell blocks script execution:

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

Then activate the environment again.

### 5️⃣ Install Dependencies

pip install -r requirements.txt

### 6️⃣ Run the Application

python app.py

### 7️⃣ Open in Browser

http://127.0.0.1:5000

---

## 🧪 Testing

The project is being tested feature-by-feature during development.

### 👨‍🎓 Student Management

- ✅ Add Student
- ✅ View Student
- ✅ Edit Student
- ✅ Delete Student
- ✅ Search Student

### 🔐 Authentication

- ✅ User Registration
- ✅ Duplicate Username Check
- ✅ Duplicate Email Check
- ✅ Password Hashing
- ✅ Login
- ✅ Logout

---

## 🏗️ Architecture

The current project follows a modular Flask architecture using separate routes, models, templates, and database components.

The planned architecture will introduce a Service Layer:

Request → Route → Service → Model → Database

### 📁 Planned Services

services/

├── auth_service.py  
└── student_service.py

The Service Layer will help separate business logic from route handling and make the application easier to maintain.

---

## 📚 Learning Outcomes

Through this project, I am practicing:

- 🐍 Python
- 🌐 Flask
- 🛣️ Routing
- 🧩 Flask Blueprints
- 📝 HTML Forms
- 🎨 CSS
- 🧠 Jinja2 Templates
- 🗄️ SQLAlchemy ORM
- 💾 SQLite
- 🔄 CRUD Operations
- 🔐 Authentication
- 🔒 Password Hashing
- 👤 Sessions
- 💬 Flash Messages
- 🧱 Application Architecture
- 🐙 Git
- 🚀 GitHub

---

## 📋 Development Roadmap

### ✅ Completed

- [x] Flask Project Setup
- [x] SQLite Database Setup
- [x] Student Model
- [x] User Model
- [x] Add Student
- [x] View Students
- [x] Edit Student
- [x] Delete Student
- [x] Search Student by Name
- [x] User Registration
- [x] Username Validation
- [x] Email Validation
- [x] Password Hashing
- [x] Login
- [x] Logout

### 🔄 In Progress

- [ ] Login Required Route Protection
- [ ] Dynamic Navigation
- [ ] Dashboard Statistics
- [ ] Advanced Form Validation
- [ ] Professional UI Improvements
- [ ] JavaScript Enhancements
- [ ] 404 Error Page
- [ ] 500 Error Page
- [ ] Application Screenshots
- [ ] Service Layer Architecture
- [ ] Final Testing

### 🚀 Future Improvements

- [ ] Pagination
- [ ] Advanced Search
- [ ] User Roles
- [ ] Admin Dashboard
- [ ] Flask-Migrate
- [ ] Unit Testing
- [ ] REST API
- [ ] Deployment

---

## 📸 Screenshots

Application screenshots will be added after the final UI and feature testing.

Planned screenshots:

- 🏠 Home Page
- 📝 Register Page
- 🔑 Login Page
- 📊 Dashboard
- ➕ Add Student
- 👨‍🎓 Student List
- 🔍 Search Student
- ✏️ Edit Student
- 🗑️ Delete Confirmation

---

## 🎓 Academic Context

This project is part of my **IIT Madras BS Degree — Diploma Level** learning journey.

It focuses on practical implementation of concepts related to:

**Modern Application Development I (MAD 1)**

The project is being developed through continuous learning, coding, testing, debugging, and architectural improvements.

---

## 👩‍💻 Author

### Saloni Tiwari

**IIT Madras BS Degree — Diploma Level**

Learning and building with:

🐍 Python  
🌐 Flask  
🗄️ Database  
🔐 Authentication  
🚀 Web Development  
🏗️ Software Architecture

---

## ⭐ Project Status

🚧 **Status: In Progress**

The project is currently under active development.

Student Management: ██████████████████░░ 90%  
Authentication: ████████████████░░░░ 85%  
Dashboard: ██████████░░░░░░░░░░ 50%  
UI & Error Handling: ████████░░░░░░░░░░░░ 40%  
Documentation: ███████████████░░░░░ 75%

---

## 📄 License

This project is created for educational and learning purposes.

---

## 🙏 Acknowledgement

This project is developed as part of my learning journey through the **IIT Madras BS Degree Programme**.

The project focuses on learning by building, testing, debugging, and gradually improving the application.

---

## ⭐ Project Journey

**Learn → Build → Test → Debug → Improve → Document → Deploy**

Built with ❤️ using **Python + Flask**.
