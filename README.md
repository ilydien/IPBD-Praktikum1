# 🚀 IPBD Praktikum 2 - Backend API

Backend API sederhana untuk sistem blog menggunakan **FastAPI**, **PostgreSQL**, dan **Docker**.
Project ini mencakup setup database, migration, dan struktur backend modular.

---

## 🧠 Tech Stack

* ⚡ FastAPI
* 🐘 PostgreSQL
* 🐳 Docker & Docker Compose
* 📦 SQLModel + SQLAlchemy
* 🔄 Alembic (Database Migration)

---

## 📁 Struktur Project

```
backend/
├── app/
│   ├── core/          # Config & utilities
│   ├── database/      # Session & model
│   ├── dto/           # Schema request/response
│   ├── routes/        # Endpoint API
│   └── main.py        # Entry point
├── migration/         # Alembic migration
├── docker-compose.yaml
├── Dockerfile
├── requirements.txt
└── pyproject.toml
```

---

## ⚙️ Cara Menjalankan Project

### 1. Clone Repository

```bash
git clone <repo-url>
cd backend
```

---

### 2. Jalankan dengan Docker

```bash
docker compose up -d --build
```

---

### 3. Akses API

Buka di browser:

```
http://localhost:8000/docs
```

---

## 🗄️ Database Migration (Alembic)

### 1. Generate Migration

```bash
alembic revision --autogenerate -m "init"
```

---

### 2. Apply Migration

```bash
alembic upgrade head
```

