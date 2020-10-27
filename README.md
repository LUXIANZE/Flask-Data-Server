# Flask Data Server

A minimalistic python based data server intends to only collect data from ReactNative client.

Flask is chosen as a lightweight server as the project might consider using various python libraries to perform data analysis in the future.

## Getting Started

- Set up a virtual environment using venv
```
python3 -m venv venv
```
- Activate the virtual environment before starting
```
. venv/bin/activate
```
- Then you should see the terminal has changed to something like 
```
(venv) username@device reponame % 
```
- Then you should install flask to be able to run the server
```
pip install -r requirements.txt
```
- To turn off the virtual environment
```
deactivate
```

## To start the development server

- In order to start your server locally, you should (assuming venv is not activated, skip first command if venv is activated)
```
. venv/bin/activate
export FLASK_APP=hello.py
flask run
```
