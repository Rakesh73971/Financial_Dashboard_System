# 💰 Financial Dashboard Backend (FastAPI)

A scalable and production-ready backend system for managing financial transactions, user roles, and dashboard analytics. Built using FastAPI, PostgreSQL, and JWT-based authentication.

---

## 🚀 Features

### 🔐 Authentication & Authorization

* User registration and login
* JWT-based authentication
* Role-Based Access Control (RBAC)

  * **Viewer** → Can view dashboard
  * **Analyst** → Can view records & insights
  * **Admin** → Full access (manage users & records)

---

### 👤 User Management

* Create and manage users
* Assign roles (Viewer, Analyst, Admin)
* Activate / Deactivate users
* Restrict actions based on roles

---

### 💳 Financial Records Management

* Create transactions (income/expense)
* View all transactions
* Update transactions
* Soft delete transactions
* Filter by:

  * Date range
  * Category
  * Type (income/expense)
* Pagination support

---

### 📊 Dashboard APIs

* Total income
* Total expenses
* Net balance
* Category-wise summary
* Monthly trends
* Recent transactions

---

### ⚙️ Additional Features

* Rate limiting (SlowAPI)
* Input validation using Pydantic
* Clean architecture (routes, services, models)
* Unit & Integration testing using Pytest

---

## 🏗️ Project Structure

```
finance-dashboard-backend/
│
├── app/
│   ├── main.py
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   ├── permissions.py
│   │   ├── limiter.py
│   │
│   ├── db/
│   │   ├── session.py
│   │   
│   │
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── routes/
│   
│
├── tests/
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/finance-dashboard-backend.git
cd finance-dashboard-backend
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup Environment Variables

Create `.env` file:

```
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_NAME=finance_db
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=yourpassword

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

### 5. Run Application

```bash
uvicorn app.main:app --reload
```

---

## 🔐 Authentication

### Register

```
POST /auth/register
```

### Login

```
POST /auth/login
```

Returns:

```
access_token
```

Use token:

```
Authorization: Bearer <token>
```

---

## 📌 API Endpoints

### 🔹 Users

* `GET /users` → List users (Admin)
* `PUT /users/{id}` → Update role/status
* `DELETE /users/{id}` → Delete user

---

### 🔹 Transactions

* `POST /records` → Create
* `GET /records` → List (with filters & pagination)
* `PUT /records/{id}` → Update
* `DELETE /records/{id}` → Soft delete

---

### 🔹 Dashboard

* `GET /dashboard/summary`
* `GET /dashboard/category`
* `GET /dashboard/monthly`
* `GET /dashboard/recent`

---

## 🧪 Running Tests

```bash
pytest
```

---

## 🛡️ Security Features

* Password hashing (bcrypt)
* JWT authentication
* Role-based access control
* Rate limiting (prevents abuse)

---

## 🧠 Design Decisions

* **Service Layer** used for business logic separation
* **Soft delete** implemented for safer data handling
* **Pagination & Filtering** for scalability
* **Modular structure** for maintainability

---

## ⚠️ Assumptions

* Each user owns their own transactions
* Role-based access is strictly enforced
* PostgreSQL is used in production

---

## 🚀 Future Improvements

* Caching (Redis)
* Docker support
* CI/CD pipeline
* API versioning
* GraphQL support

---

## 👨‍💻 Author

**Rakesh N**

---

## ⭐ Contribution

Feel free to fork, improve, and raise pull requests!
