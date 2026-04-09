# FastAPI Auth + Listing API

## Features
- User Registration
- User Login (JWT Authentication)
- Password Hashing
- Protected Routes (Bearer Token)
- User-specific Listings (each user sees their own data)

## Authentication

1. Register a user using `/user/register`
2. Login using `/user/login` to get access token
3. Use the token in Swagger Authorize button
4. Access protected endpoints like `/listing/`

Example:
Bearer <your_token>

## API Endpoints

### User
- POST /user/register
- POST /user/login

### Listings (Protected)
- POST /listing/
- GET /listing/

## Tech Stack
- FastAPI
- SQLAlchemy
- SQLite
- JWT (python-jose)
- Passlib (bcrypt)

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload