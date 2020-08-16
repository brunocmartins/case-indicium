FROM ubuntu:18.04

COPY requirements.txt ./

# Install python 3 and pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# Update pip and install required libraries
RUN pip3 install --upgrade pip && \
    pip3  install --no-cache-dir -r requirements.txt

COPY case.py ./
COPY data ./data

CMD ["python3", "./case.py"]