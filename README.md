# python-demo
Flask application with 90K methods,300 files where each file contains 300 method.
to create more files update the *FILES_NUMBER* variable inside *create.sh* . to increase the number of methods in each file update *METHODS_NUMBER* variable.make sure to increase the range number inside the for loop in app.py file to be the number of the files+1.


when navigating to 127.0.0.1:5000 it will call all the 20K methods.
to run the application :
```shell
python3 -m flask run --host=0.0.0.0
```
to run with Sealights:
```shell
export BSID=$(cat buildSessionId.txt)
export SL_TOKEN=your_lab_token
sl-python run --token $SL_TOKEN --buildsessionid $BSID python3 -m flask run --host=0.0.0.0
```

to run test  :
```shell
curl -X POST   http://127.0.0.1:5000/add   -H 'Content-Type: application/json'   -d '{
    "numbers": [5, 10, 30]
}'
```
