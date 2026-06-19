# ⚡ Todo CRUD API with Pydantic Validation — Day 21 FastAPI Challenge

**Issue:** [#393](https://github.com/abhishek-goswami1/Daily-Dev-Challenges/issues/393) | Week 3 | Beginner

## 📋 Description

Full CRUD REST API for todos with Pydantic validation. In-memory store. Testable via Swagger UI at `/docs`.

## ✨ Endpoints
| Method | Path | Description |
|--------|------|-------------|
| GET | `/todos` | List all |
| GET | `/todos/{id}` | Get one |
| POST | `/todos` | Create |
| PUT | `/todos/{id}` | Update |
| DELETE | `/todos/{id}` | Delete |

## 🚀 How to Run
```bash
pip install fastapi uvicorn && uvicorn main:app --reload
```
