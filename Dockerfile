# Base image
FROM python:3.9-slim

# Set work directory and copy requirements
WORKDIR /app
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY api/ ./api/
COPY core/ ./core/
COPY tests/ ./tests
COPY main.py .

# Expose the port and run the application
EXPOSE 8000

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
