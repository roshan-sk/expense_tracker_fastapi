# Expense Tracker FastAPI

A simple **Expense Tracker API** built with **FastAPI**, allowing users to manage and track personal expenses.

## Deployed URL
[https://expensestrackerfastapi.up.railway.app](https://expensestrackerfastapi.up.railway.app)

## Features
- User registration and login (JWT authentication)
- Create, read, update, and delete personal expenses
- Track expenses by title, amount, category, and date
- User profile endpoint to fetch logged-in user details

## Tech Stack
- **Backend:** FastAPI
- **Database:** SQLite (for testing), PostgreSQL recommended for production
- **Authentication:** JWT tokens
- **Deployment:** Railway (Free Tier)

## API Endpoints

| Endpoint           | Method | Description |
|-------------------|--------|-------------|
| `/auth/register`   | POST   | Register a new user |
| `/auth/login`      | POST   | Login and receive JWT token |
| `/auth/me`         | GET    | Get current user profile (requires token) |
| `/expenses/`       | GET    | List all expenses of the current user |
| `/expenses/`       | POST   | Create a new expense |
| `/expenses/{id}`   | PUT    | Update an existing expense |
| `/expenses/{id}`   | DELETE | Delete an expense |

## Headers for protected endpoints

Authorization: Bearer <your_access_token>
Content-Type: application/json



## Deployment Process

1. Prepare project
   - Ensure `requirements.txt` is up-to-date: `pip freeze > requirements.txt`
   - SQLite database path is relative: `sqlite:///./expense.db`
2. Push code to GitHub
3. Create a Railway project and deploy from GitHub
4. Set start command (Procfile or Railway settings):
    web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
5. Deploy → Railway will provide a public URL
6. Test endpoints using Postman or curl

## Postman Tip
- Create environment variable: `BASE_URL = https://expensestrackerfastapi.up.railway.app`
- Use `{{BASE_URL}}/auth/login` for API calls

---

**Author:** Roshan Sk  
**Contact:** roshansk032@gmail.com
