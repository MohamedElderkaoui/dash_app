# Use official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the app files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 8050 for Dash
EXPOSE 8050

# Run the Dash app
CMD ["python", "app.py"]
