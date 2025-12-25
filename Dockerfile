# Gunakan Python versi ringan
FROM python:3.9-slim

# Set folder kerja di dalam container
WORKDIR /app

# Copy file requirements dulu (biar cache efisien)
COPY requirements.txt .

# Install library
RUN pip install --no-cache-dir -r requirements.txt

# Copy sisa codingan (app.py)
COPY . .

# Buka port 80
EXPOSE 80

# run
CMD ["python", "app.py"]
