# FastAPI Blog API with Authentication

A RESTful Blog API built using **FastAPI** that supports **user authentication and blog CRUD operations**.
The application uses **SQLite as the database** and **SQLAlchemy ORM** for database interaction.

This project demonstrates backend development concepts such as API routing, authentication, dependency injection, and database management.

---

## Features

* User Registration
* User Login with JWT Authentication
* Create Blog Posts
* View All Blogs
* View Blog by ID
* Update Blog
* Delete Blog
* Password Hashing
* SQLite Database Integration
* RESTful API Design

---

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* JWT Authentication
* Passlib (Password Hashing)
* Uvicorn (ASGI Server)

---

## Project Structure

```
fastapi-blog-api-with-auth
│
├── blog
│   ├── repository
│   │   ├── blog.py
│   │   └── user.py
│   │
│   ├── routers
│   │   ├── authentication.py
│   │   ├── blog.py
│   │   └── user.py
│   │
│   ├── database.py
│   ├── hashing.py
│   ├── models.py
│   ├── oauth2.py
│   ├── schemas.py
│   └── token.py
│
├── blog.db
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

### 1 Clone the repository

```
git clone https://github.com/yourusername/fastapi-blog-api-with-auth.git
```

### 2 Go to the project folder

```
cd fastapi-blog-api-with-auth
```

### 3 Create virtual environment

```
python -m venv venv
```

Activate it

Windows

```
venv\Scripts\activate
```

Mac / Linux

```
source venv/bin/activate
```

---

## Install Dependencies

```
pip install -r requirements.txt
```

---

## Run the Application

Start the FastAPI server:

```
uvicorn main:app --reload
```

The API will run at:

```
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI provides automatic interactive API documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| POST   | /login   | User login  |

---

### User

| Method | Endpoint   | Description    |
| ------ | ---------- | -------------- |
| POST   | /user      | Create user    |
| GET    | /user/{id} | Get user by ID |

---

### Blog

| Method | Endpoint   | Description    |
| ------ | ---------- | -------------- |
| GET    | /blog      | Get all blogs  |
| POST   | /blog      | Create blog    |
| GET    | /blog/{id} | Get blog by ID |
| PUT    | /blog/{id} | Update blog    |
| DELETE | /blog/{id} | Delete blog    |

---

## Database

This project uses **SQLite** as the database.

Database file:

```
blog.db
```

SQLAlchemy ORM is used for database interaction.

---

## Run with Reload (Development Mode)

```
uvicorn main:app --reload
```

This automatically reloads the server when code changes.

---

## Author

Karthi Keyan

Backend Developer | Python | FastAPI
