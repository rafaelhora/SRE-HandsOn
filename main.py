#This program receives a string with a URL, the SLO for successful responses (double) and its the SLO for response time (double)
#Makes a HTTP GET request every 5 seconds and calculates the current SLIs.
#It displays for each URL the current SLIs, the SLOs and wheter the SLOs are being met

import requests #Library that will handle the HTTP requests
import time
from flask import Flask, render_template     #All Flask stuff
from flask import request

app = Flask(__name__)

@app.route('/sup') #DEBUG page, serves to see if basic server cfgs are working
def hello_world():
    return 'Hello inloco!'

@app.route('/') #Main page, will get the URL and the desired SLOs
def index():
    return render_template('index.html') #This will render index.html for the user when localhost:5000/ is requested
@app.route('/', methods = ['POST']) #Placeholder, the program recognises the forms entries
def showsInputUrl():
    url = request.form['userUrl']
    successSLO = request.form['userSLOSuccess']
    timeSLO = request.form['userSLOSpeed']
    text = url + ', ' + str(successSLO) + ', ' + str(timeSLO)
    print text
    return text

@app.route('/sli') #Error: 500 internal error, can't seem to make the requests library to work
def get_data():
    #return 'hey man'
    start = time.time()
    r = requests.get('https://facebook.com')
    responseTime = time.time() - start
    print responseTime #prints the respose time between before the request and after receiving the headers
    print r.status_code #returns the status of the request (200 for sucess)
    return 'success'
if __name__ == '__main__': #The script that is going to be executed
    app.run(debug = True) #This facilitates development since you don't have to restart everything for every time you change your app, similar to nodejs
