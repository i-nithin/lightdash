import os
import uuid
import random
from datetime import timedelta, datetime
import psycopg2
from faker import Faker
from tqdm import trange
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("PGUSER")
DB_PASSWORD = os.getenv("PGPASSWORD")
DB_HOST = os.getenv("PGHOST")
DB_PORT = os.getenv("DB_PORT", 5432)
DB_NAME = os.getenv("PGDATABASE")

DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?sslmode=require"

fake = Faker()

NUM_USERS = 500
SOURCES = ['Google', 'Facebook', 'Organic', 'Referral', 'LinkedIn']
PAGES = ['landing', 'pricing', 'features', 'blog', 'signup']

def connect_db():
    return psycopg2.connect(DB_URL)

def create_tables(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id UUID PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                signup_date DATE NOT NULL,
                source TEXT NOT NULL
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                id UUID PRIMARY KEY,
                user_id UUID REFERENCES users(id),
                start_date DATE NOT NULL,
                end_date DATE,
                price_usd DECIMAL NOT NULL
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS payments (
                id UUID PRIMARY KEY,
                user_id UUID REFERENCES users(id),
                amount DECIMAL NOT NULL,
                payment_date DATE NOT NULL
            );
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS visits (
                id UUID PRIMARY KEY,
                user_id UUID,
                visit_date DATE NOT NULL,
                page TEXT
            );
        """)
        conn.commit()

def generate_data(conn):
    with conn.cursor() as cur:
        start_date = datetime.today() - timedelta(days=180)

        for _ in trange(NUM_USERS, desc="Generating users"):
            user_id = str(uuid.uuid4())
            name = fake.name()
            email = fake.email()
            signup_date = start_date + timedelta(days=random.randint(0, 180))
            source = random.choice(SOURCES)

            cur.execute("INSERT INTO users (id, name, email, signup_date, source) VALUES (%s, %s, %s, %s, %s)",
                        (user_id, name, email, signup_date, source))

            for _ in range(random.randint(1, 20)):
                visit_date = signup_date + timedelta(days=random.randint(0, 60))
                page = random.choice(PAGES)
                cur.execute("INSERT INTO visits (id, user_id, visit_date, page) VALUES (%s, %s, %s, %s)",
                            (str(uuid.uuid4()), user_id, visit_date, page))

            if random.random() < 0.7:
                price = random.choice([29, 49, 99])
                start = signup_date + timedelta(days=random.randint(1, 10))
                end = None if random.random() < 0.8 else start + timedelta(days=random.randint(30, 180))
                sub_id = str(uuid.uuid4())
                cur.execute("""
                    INSERT INTO subscriptions (id, user_id, start_date, end_date, price_usd)
                    VALUES (%s, %s, %s, %s, %s)
                """, (sub_id, user_id, start, end, price))

                for i in range(random.randint(1, 6)):
                    pay_date = start + timedelta(days=30 * i)
                    if pay_date > datetime.today():
                        break
                    cur.execute("""
                        INSERT INTO payments (id, user_id, amount, payment_date)
                        VALUES (%s, %s, %s, %s)
                    """, (str(uuid.uuid4()), user_id, price, pay_date))

        conn.commit()

if __name__ == "__main__":
    conn = connect_db()
    create_tables(conn)
    generate_data(conn)
    conn.close()
    print("✅ Data generation complete.")
