# 📈 Stock Alert API

A clean, production‑style **FastAPI backend** that monitors stock price movements, fetches related news, and triggers alerts when significant changes occur.

This project is inspired by the *100 Days of Python* stock alert challenge, but is intentionally structured like a **real backend service**, not a tutorial script.

---

## 🚀 Features

- 📊 Fetch daily stock prices from a stock market API
- 📰 Retrieve recent news articles related to a company
- 🚨 Trigger alerts when price movement exceeds a threshold
- 🌐 REST API with interactive Swagger docs
- 🧱 Clean architecture (services, domain logic, API layer)
- 🔁 Easily extensible to mobile apps, schedulers, or notifications

---

## 🧠 Architecture Overview

```
Mobile App / Web Client
        ↓
   FastAPI Backend
        ↓
 External APIs (Stocks, News)
```

The backend is **stateless**, JSON‑based, and designed to be consumed by:
- Mobile apps (Flutter / React Native)
- Web frontends
- Schedulers / cron jobs

---

## 📁 Project Structure

```
stock-alert-app/
├── .env
├── README.md
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── constants.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── stock_service.py
│   │   ├── news_service.py
│   │   └── notification_service.py
│   └── domain/
│       ├── __init__.py
│       └── stock_alert.py
└── tests/
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone & Create Virtual Environment

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

### 2️⃣ Install Dependencies

```powershell
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the **project root**:

```
STOCK_API_KEY=your_stock_api_key_here
NEWS_API_KEY=your_news_api_key_here
```

> ⚠️ Do not commit `.env` to source control.

The app loads environment variables using `python-dotenv`.

---

## ▶️ Running the Application

From the **project root**:

```powershell
uvicorn app.main:app --reload
```

The API will be available at:

```
http://localhost:8000
```

Interactive API docs:

```
http://localhost:8000/docs
```

---

## 🌐 API Endpoints

### ✅ Health Check

```
GET /health
```

Response:
```json
{ "status": "ok" }
```

---

### 📊 Stock Price Change

```
GET /stock/change
```

Returns latest vs previous close and percentage change.

---

### 📰 Company News

```
GET /news
```

Returns top recent news articles for the configured company.

---

### 🚨 Run Alert Logic

```
POST /alert/run
```

Runs the full alert flow:
- Fetch stock prices
- Check threshold
- Fetch news
- Send notification

---

## 🧩 Design Principles

- **Separation of concerns**
- **Dependency inversion** (services injected into domain logic)
- **Replaceable implementations** (APIs, notifications)
- **Backend‑first design** suitable for mobile apps

---

## 📱 Mobile App Ready

This backend is designed to power:
- Flutter apps
- React Native apps
- Native iOS / Android apps

All communication happens via HTTPS + JSON.

---

## 🔔 Notifications

The current `NotificationService` outputs alerts to the console.

It can be replaced with:
- SMS (Twilio)
- Email
- Push notifications (Firebase / OneSignal)
- Slack / Teams webhooks

No changes to business logic required.

---

## 🛠️ Future Improvements

- Async HTTP calls (`httpx`)
- JWT authentication
- User accounts & saved stocks
- Background scheduler (daily checks)
- Caching to avoid API rate limits
- Mobile push notifications

---

## 🧪 Testing

Unit tests can be added by:
- Mocking external APIs
- Testing domain logic independently

The architecture is designed for **testability**.

---

## 🙌 Author

Built as a learning‑to‑production backend project using **FastAPI** and clean Python architecture principles.

