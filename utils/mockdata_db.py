import sqlite3
import pandas as  pd
from faker import Faker
import random
from datetime import datetime,timedelta

fake=Faker()

import sqlite3
import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Data basega  ulanish
conn = sqlite3.connect('bank.db')
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

# Mock data: 100ming mijoz
num_clients = 100000
clients = []
for i in range(1, num_clients + 1):
    clients.append((i, fake.name(), fake.date_of_birth(minimum_age=18, maximum_age=80), random.choice(['Toshkent', 'Jizzax', 'Samarqand', 'Buxoro', 'Xorazm', 'Andijon', 'Sirdaryo'])))

pd.DataFrame(clients, columns=['id', 'name', 'birth_date', 'region']).to_sql('Clients', conn, if_exists='replace', index=False)