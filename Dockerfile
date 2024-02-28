FROM python:3.11.8-alpine3.19

COPY . . 
RUN pip install Flask
RUN pip install sealights-python-agent
EXPOSE 5000
# CMD ["python3","app.py"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]