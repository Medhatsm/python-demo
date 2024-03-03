FROM python:3.11.8-alpine3.19


RUN pip install Flask
RUN pip install sealights-python-agent==2.0.0b2
WORKDIR /app
COPY . . 

EXPOSE 5000
# CMD ["python3","app.py"]
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD ["/bin/sh","-c","sl-python run --token $SL_TOKEN --buildsessionid $BSID python3 -m flask run --host=0.0.0.0"]

