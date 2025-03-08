# Use the latest stable Python version
FROM python:3.12

# Prevent Python from buffering output
ENV PYTHONUNBUFFERED=1

# Update package lists and install necessary dependencies
RUN apt-get update && apt-get install -y gettext

# Load environment variables
ARG ENVIRONMENT
ENV ENVIRONMENT=${ENVIRONMENT}
RUN echo ${ENVIRONMENT}

# Create and set the working directory
RUN mkdir /src
WORKDIR /src

# Build argument (only available during build)
ARG ENVIRONMENT=production

# Set environment variable for runtime
ENV ENVIRONMENT=${ENVIRONMENT}

# Debug: Print environment variable
RUN echo "ENVIRONMENT during build: ${ENVIRONMENT}"

# Copy dependencies and install them based on the environment
COPY requirements.txt requirements-dev.txt /src/

# Install dependencies and print installed packages
RUN if [ "$ENVIRONMENT" = "development" ]; then \
        echo "Installing development dependencies..."; \
        pip install --upgrade pip && pip install -r /src/requirements-dev.txt; \
    else \
        echo "Installing production dependencies..."; \
        pip install --upgrade pip && pip install -r /src/requirements.txt; \
    fi

# Copy the application source code
COPY . /src
