FROM python:3.7
#base image: 3.7 py ..look at using python:3-alphine as its light weight and faster 
RUN mkdir -p /bookcatalog/app

WORKDIR /bookcatalog/app
COPY . /bookcatalog/app
RUN pip install --no-cache-dir -r requirements.txt

#ENV PORT 8890
EXPOSE 8890
#VOLUME ["/app-data"]
CMD ["python", "api.py"]
