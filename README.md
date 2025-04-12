# 📊 SaaS Growth Analytics Dashboard – Powered by Lightdash + dbt

A data analytics dashboard for monitoring key SaaS metrics including user growth, payments, subscriptions, and user visits. Built with a modular data warehouse schema and visualized through an interactive UI.

# 1. What Is This Project?

This is a full-stack BI demo project simulating SaaS business metrics, powered by:

- Python for data generation
- PostgreSQL as the warehouse
- dbt for modeling
- Lightdash as the analytics layer

I built this to explore how Lightdash can help teams define metrics once and empower everyone to explore data independently.

## 📊 Key Metrics Tracked

### User Metrics

- **Total Users** – Count of all registered users
- **Signup Source Breakdown** – Users by acquisition channel (organic, paid ads, referrals)
- **Total Visits** – Number of website visits

### Revenue Metrics

- **Total Payments** – Number of payment transactions
- **Total Revenue** – Sum of all payment amounts
- **Total Subscriptions** – Number of active and past subscriptions

### Conversion Performance

- **Signup → Payment Conversion**  
  Funnel showing:
  - Total signups → Users who made at least one payment
  - Conversion rate between stages

## ⚙️ Setup (Without Docker)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/i-nithin/lightdash.git
cd saas-analytics
```

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate        # For Linux/macOS
# OR
.venv\Scripts\activate           # For Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Create a `.env` File

````ini
# Individual connection parameters (recommended)
PGHOST=your-db-host.neon.tech
PGDATABASE=your_database_name
PGUSER=your_user
PGPASSWORD=your_password
PGPORT=5432
````
### 5️⃣ Run the Mock Data Generator

```bash
python3 data_gen/load_mock_data.py

This script will:
 - Create tables if not exist
 - Insert fake user, visit, subscription & payment data
```

## 🥪 Sample Tables Created

- `users`
- `subscriptions`
- `payments`
- `visits`

## 📊 Live Dashboard Example

A sample dashboard generated using this mock data is available on Lightdash:

[![Lightdash Dashboard](https://img.shields.io/badge/View-Lightdash_Dashboard-blue?style=for-the-badge&logo=lightdash)](https://app.lightdash.cloud/projects/35436cc1-00f4-452b-99f0-4cf596dd2eef/dashboards/65323ed2-9472-4ac7-a226-eccfc1a953e4/view)
