FROM python:3.11

WORKDIR /app

# Copy only requirements first for better caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the application
COPY . .

EXPOSE 8516

CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8516"]