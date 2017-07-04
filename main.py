#This program receives a string with a URL, the SLO for successful responses (double) and its the SLO for response time (double)
#Makes a HTTP GET request every 5 seconds and calculates the current SLIs.
#It displays for each URL the current SLIs, the SLOs and wheter the SLOs are being met

import requests #Library that will handle the HTTP requests
import time
from flask import Flask    #All Flask stuff
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/sup') #DEBUG page, serves to see if basic server cfgs are working
def hello_world():
    return 'Hello inloco!'

@app.route('/') #Main page, will get the URL and the desired SLOs
def index():
    return render_template('index.html') #This will render index.html for the user when localhost:5000/ is requested

@app.route('/sreTester', methods = ['POST']) #Placeholder, the program recognises the forms entries
def testSLI():
    url = request.form['userUrl']
    successSLO = request.form['userSLOSuccess']
    speedSLO = request.form['userSLOSpeed']
    speedSLOMet = 0
    successSLOMet = 0
    iterations = 0
    while(True):
        testIteration = requests.get(url)
        speedSLI = testIteration.elapsed.total_seconds()
        successSLI = testIteration.status_code

        if speedSLI <= 1.0: #not working properly don't know why, numbers conflicting maybe
            speedSLOMet += 1
        if successSLI > 199:
            if successSLI < 500:
                successSLOMet += 1

        iterations += 1

        successPercentage = successSLOMet/iterations * 100
        speedPercentage = speedSLOMet/iterations * 100 # returning always zero somehow

        if successPercentage <= successSLO: # not working properly giving the opposed result, bruteforced inverting the logic
            successFeedback = 'SLO OK!'
        else:
            successFeedback = 'SLO NOT OK!'

        if speedPercentage <= speedSLO: #bruteforced inverting the logic
            speedFeedback = 'SLO OK!'
        else:
            speedFeedback = 'SLO NOT OK!'

        print ('iteration: '+ str(iterations) + ' ' + url + ' Status:' + str(successSLI) +', Successful requests SLI:' + str(successPercentage) +'% ('+ successFeedback + ')' + '. Response time:' + str(speedSLI) +'sec, Responses in less than 100ms SLI:' + str(speedPercentage) + '% (' + speedFeedback + ')')

        time.sleep(5)
    #print (url)
    #return url

#@app.route('/sli') #Error: 500 internal error, can't seem to make the requests library to work
#def get_data():
#    #return 'hey man'
#    for i in range(0,10):
#        start = time.time()
#        r = requests.get('https://httpbin.org/anything')
#        responseTime = time.time() - start
#        print responseTime #prints the respose time between before the request and after receiving the headers
#        print r.status_code #returns the status of the request (200 for sucess)
#    return 'success'
if __name__ == '__main__': #The script that is going to be executed
    app.run(debug = True) #This facilitates development since you don't have to restart everything for every time you change your app, similar to nodejs
