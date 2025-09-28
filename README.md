# Bank_Task  
🧑‍💻 **Data Analyst Assistant**

AI yordamida foydalanuvchi savollarini SQL so‘roviga aylantiruvchi yordamchi dastur.  
Streamlit web-interfeysi orqali foydalanuvchi savol kiritadi, dastur esa uni **Ollama** (`llama3` modeli) orqali SQL so‘rovga aylantirib beradi.

---

## ⚙️ O‘rnatish

### 1. Repozitoriyani klonlash
```bash
git clone https://github.com/baxronovferuz1/Bank_Task.git
cd Bank_Task
```

### 2. Ollama o‘rnatish

Loyihani ishlatish uchun **Ollama server** kerak bo‘ladi. Rasmiy sayt va o‘rnatish bo‘yicha ko‘rsatmalar: [https://ollama.ai](https://ollama.ai)

Ollama o‘rnatib,kerakli modelni yuklash:

```bash
ollama pull llama3
```


### 3. Docker bilan ishga tushirish

Docker va Docker Compose o‘rnatilgan bo‘lsa:

```bash
docker-compose up --build
```

Server ishga tushgach, Streamlit ilovasini brauzerda oching:

👉 `http://localhost:8501`

Docker konteynerlarni to‘xtatish:

```bash
docker-compose down
```

Konteyner loglarini ko‘rish:

```bash
docker-compose logs -f
```


## 🌐 Foydalanish (Usage)

Brauzerda oching:

`http://localhost:8501`

Ilovaga savol yozing; masalan:

> `2025 yil iyun oyida Toshkent viloyati bo‘yicha jami tranzaksiyalar summasini ko‘rsat`

Javob sifatida sizga mos **SQL so‘rovi** qaytariladi.

---

## 💡 Misol so‘rovlar (Examples)

**Savol:**

```
2025 yil iyun oyida Toshkent viloyati bo‘yicha jami tranzaksiyalar summasini ko‘rsat
```

**Kutilgan natija (misol):**

```sql
SELECT SUM(amount) AS total
FROM transactions
WHERE region = 'Toshkent' AND EXTRACT(MONTH FROM transaction_date) = 6 AND EXTRACT(YEAR FROM transaction_date) = 2025;
```

> Natijani Excel formatida ham yuklab olishingiz mumkin

---

![Task.db natijasi](https://files.uzgeouniver.uz/media/files/task_db_result.jpg)

![Exceldagi natija](https://files.uzgeouniver.uz/media/files/excel_result.jpg)

![Localhostdagi natija](https://files.uzgeouniver.uz/media/files/locahostdagi_natija.jpg)

## 📜 Litsenziya (License)

Bu loyiha **MIT License** ostida tarqatiladi. To‘liq matn `LICENSE` faylida mavjud bo‘lishi kerak.

---
