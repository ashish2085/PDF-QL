# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Create a non-root user with a UID between 10000 and 20000
RUN groupadd -g 10001 appgroup && \
    useradd -m -u 10001 -g appgroup appuser

# Set permissions and switch to non-root user
RUN chown -R appuser:appgroup /app
USER 10001

# Copy application files
COPY . /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose the Streamlit port
EXPOSE 8501

# Set the Streamlit configuration to listen on all interfaces
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ENABLECORS=false

# Set the entry point using python -m streamlit
ENTRYPOINT ["python", "-m", "streamlit", "run", "app.py", "--server.address=0.0.0.0"]
