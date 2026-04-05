# 💰 Financial Dashboard Backend (FastAPI)

A scalable backend system for managing financial transactions, user roles, and analytics. Built with FastAPI, PostgreSQL, and JWT authentication following clean architecture principles.

---

## 🚀 Tech Stack

* **Backend Framework**: FastAPI
* **Language**: Python
* **Database**: PostgreSQL
* **ORM**: SQLAlchemy
* **Authentication**: JWT (Token-based)
* **Validation**: Pydantic
* **Testing**: Pytest
* **Rate Limiting**: SlowAPI

---

## 🔐 Authentication & Authorization

* JWT-based login system
* Secure password hashing
* Role-Based Access Control (RBAC)

### Roles:

* **Viewer** → View dashboard only
* **Analyst** → Access transactions & insights
* **Admin** → Full system control

---

## 👤 User Management APIs

| Method | Endpoint      | Description          | Access |
| ------ | ------------- | -------------------- | ------ |
| GET    | `/users/`     | Get all users        | Admin  |
| GET    | `/users/me`   | Current user profile | All    |
| PATCH  | `/users/{id}` | Update role/status   | Admin  |

---

## 🔐 Auth APIs

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| POST   | `/auth/register` | Register user     |
| POST   | `/auth/login`    | Login & get token |

---

## 💳 Transaction APIs

| Method | Endpoint             | Description                            | Access |
| ------ | -------------------- | -------------------------------------- | ------ |
| POST   | `/transactions/`     | Create transaction                     | Admin  |
| GET    | `/transactions/`     | Get transactions (filter + pagination) | All    |
| PUT    | `/transactions/{id}` | Update transaction                     | Admin  |
| DELETE | `/transactions/{id}` | Delete transaction                     | Admin  |

### Filters Supported:

* Type (income/expense)
* Category
* Date range

### Pagination:

* `skip`
* `limit`

---

## 📊 Dashboard APIs

| Method | Endpoint              | Description                    |
| ------ | --------------------- | ------------------------------ |
| GET    | `/dashboard/summary`  | Total income, expense, balance |
| GET    | `/dashboard/category` | Category-wise totals           |
| GET    | `/dashboard/monthly`  | Monthly trends                 |
| GET    | `/dashboard/recent`   | Recent transactions            |

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone <repo-url>
cd project-folder
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment (.env)

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

### 5. Run Server

```bash
uvicorn app.main:app --reload
```

---

## 🧪 Running Tests

```bash
pytest
```

---

## 🛡️ Security & Reliability

* JWT authentication
* Role-based authorization
* Rate limiting on APIs
* Input validation
* Error handling
* Soft delete for data safety

---

## 🧠 Design Decisions

* Service layer for business logic separation
* Modular structure for scalability
* Pagination for large datasets
* Filters for flexible querying

---

## ⚠️ Assumptions

* Each user accesses only their own data
* Admin controls user roles and permissions
* Transactions are user-specific

---

## 🔄 Trade-offs

* Used synchronous SQLAlchemy instead of async (simpler implementation)
* PostgreSQL used instead of NoSQL for structured financial data
* Rate limiting per IP instead of per user (simpler setup)

---

## 🚀 Future Improvements

* Redis caching
* Docker deployment
* Async DB support
* API versioning
* CI/CD pipeline

---

## 👨‍💻 Author

**Rakesh N**
