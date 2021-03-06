FROM python

ENV PYTHONUNBUFFERED 1

#set a directory for the app
WORKDIR /usr/app

RUN pip install --upgrade pip
#copy all the files to the container
COPY . .

#install dependencies
RUN pip install -r requirements.txt

#expose the port of the container
EXPOSE 8000

#run command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]