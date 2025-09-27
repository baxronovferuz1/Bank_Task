FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# Kutubxonalarni o‘rnatiw
RUN pip install --no-cache-dir -r requirements.txt


COPY . .

# Streamlitni porti(8501)
EXPOSE 8501


CMD ["streamlit", "run", "utils/web_interface.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableCORS=false"]

