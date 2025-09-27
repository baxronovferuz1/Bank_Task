import sqlite3
import pandas as  pd
from faker import Faker
import random
from datetime import datetime,timedelta

fake=Faker()


# Data basega  ulanish
conn = sqlite3.connect('task.db')
cur = conn.cursor()

# Tablitsalani yaratish qismi
cur.execute('''CREATE TABLE IF NOT EXISTS Clients (
    id INTEGER PRIMARY KEY,
    name TEXT,
    birth_date DATE,
    region TEXT
)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Accounts (
    id INTEGER PRIMARY KEY,
    client_id INTEGER,
    balance REAL,
    open_date DATE,
    FOREIGN KEY(client_id) REFERENCES Clients(id)
)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Transactions (
    id INTEGER PRIMARY KEY,
    account_id INTEGER,
    amount REAL,
    date DATE,
    type TEXT,
    FOREIGN KEY(account_id) REFERENCES Accounts(id)
)''')


num_clients = 1000
clients = []
for i in range(1, num_clients + 1):
    clients.append((i, fake.name(), fake.date_of_birth(minimum_age=18, maximum_age=80), random.choice(["Toshkent","Jizzax","Samarqand","Buxoro","Xorazm","Andijon","Sirdaryo","Navoiy","Surxandaryo","Qashqadaryo","Fargona","Namangan"])))

pd.DataFrame(clients, columns=['id', 'name', 'birth_date', 'region']).to_sql('Clients', conn, if_exists='replace', index=False)


num_accounts = 5000
accounts = []
for i in range(1, num_accounts + 1):
    accounts.append((i, random.randint(1, num_clients), random.uniform(1000, 100000), fake.date_between(start_date='-5y', end_date='today')))

pd.DataFrame(accounts, columns=['id', 'client_id', 'balance', 'open_date']).to_sql('Accounts', conn, if_exists='replace', index=False)


num_transactions = 10000
transactions = []
for i in range(1, num_transactions + 1):
    date = fake.date_between(start_date='-4y', end_date='today')
    transactions.append((i, random.randint(1, num_accounts), random.uniform(-5000, 5000), date, random.choice(['deposit', 'withdraw', 'transfer'])))

pd.DataFrame(transactions, columns=['id', 'account_id', 'amount', 'date', 'type']).to_sql('Transactions', conn, if_exists='replace', index=False)

conn.commit()
conn.close()
print("DB created! File: task.db")