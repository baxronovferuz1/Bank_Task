import ollama
import os

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://host.docker.internal:11434")


def generate_sql(prompt):
    db_schema = """
    Tablitsalar:
    - Clients (id INTEGER, name TEXT, birth_date DATE, region TEXT)
    - Accounts (id INTEGER, client_id INTEGER, balance REAL, open_date DATE)
    - Transactions (id INTEGER, account_id INTEGER, amount REAL, date DATE, type TEXT)

    Muhim: Region Clients da. Tranzaksiyalar bo'yicha region olish uchun JOIN ishlat: Transactions t JOIN Accounts a ON t.account_id = a.id JOIN Clients c ON a.client_id = c.id
    Sana uchun: strftime('%m', date) = '06' va strftime('%Y', date) = '2024' ishlat (EXTRACT emas).
    Region text, shuning uchun c.region = 'Toshkent'
    """

    few_shots = """
    Misol 1:
    Savol: "Jami balansni ko'rsat"
    SQL: SELECT SUM(balance) FROM Accounts;
    
    Misol 2:
    Savol: "Toshkent mijozlari sonini ko'rsat"
    SQL: SELECT COUNT(*) FROM Clients WHERE region = 'Toshkent';
    
    Misol 3:
    Savol: "2024 yil iyun oyida Toshkent bo'yicha tranzaksiyalar summasini ko'rsat"
    SQL: SELECT SUM(t.amount) FROM Transactions t JOIN Accounts a ON t.account_id = a.id JOIN Clients c ON a.client_id = c.id WHERE c.region = 'Toshkent' AND strftime('%m', t.date) = '06' AND strftime('%Y', t.date) = '2024';
    """


    full_prompt = f"""
    Sen SQL expertisan. Foydalanuvchi savolini SQL query ga aylantir.
    {db_schema}
    {few_shots}
    Savol: {prompt}
    Javobda faqat SQL query yoz, hech qanday izohsiz. Misol: SELECT ... FROM ...
    Agar savol noto'g'ri bo'lsa, 'Invalid query' deb yoz.
    """
    response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': full_prompt}])
    return response['message']['content'].strip()


if __name__ == "__main__":
    prompt = "2024 yil iyun oyida Toshkent viloyati bo‘yicha jami tranzaksiyalar summasini ko‘rsat"
    print(generate_sql(prompt))

