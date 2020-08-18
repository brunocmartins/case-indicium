FROM python:3

LABEL maintainer="brunocmartins4@gmail.com"

COPY requirements.txt /costabrunom/case_indicium/
COPY case.py /costabrunom/case_indicium/
COPY data /costabrunom/case_indicium/data

WORKDIR /costabrunom/case_indicium

# Install required libraries
RUN pip  install --no-cache-dir -r requirements.txt

CMD ["python3", "./case.py"]