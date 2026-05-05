FROM python:3.11-slim

# Create non-root user for Hugging Face Spaces
RUN useradd -m -u 1000 user

USER user

ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /app

# Copy and install dependencies first for better Docker caching
COPY --chown=user requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY --chown=user . .

# Hugging Face Spaces expects apps to run on port 7860
EXPOSE 7860

# Start the app
CMD ["python", "app.py"]
