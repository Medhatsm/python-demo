# python-demo
Flask application with 20K methods,100 files where each file contains 200 method.
to create more files update the *FILES_NUMBER* variable inside *create.sh* . to increase the number of methods in each file update *METHODS_NUMBER* variable.make sure to increase the range number inside the for loop in app.py file to be the number of the files+1.


when navigating to 127.0.0.1:5000 it will call all the 20K methods.
to run the application :
```shell
python3 -m flask run --host=0.0.0.0
```

