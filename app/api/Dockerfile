# Use a more recent version of Python
FROM python:3.9-slim

# Install necessary build tools and libraries
# RUN apk add --no-cache build-base gcc gfortran musl-dev linux-headers libgfortran lapack-dev freetype-dev libpng-dev openblas-dev

# ERROR
# The error message indicates that the build process for scikit-learn 1.5.0 
# is failing because the necessary compilers (e.g., gcc, clang) are not installed in the Docker image.
# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

## setup working directory

# Copy requirements file
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt
#RUN pip install --upgrade pip && \
#   pip install -r requirements.txt

#RUN python -c "import nltk; nltk.download('omw-1.4'); nltk.download('wordnet')"

# Copy the rest of the application code
COPY  . .

# Expose port
EXPOSE 5000

# define environment veriable
# ENV NAME World

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

