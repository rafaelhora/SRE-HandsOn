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

@app.route('/sreTester', methods = ['POST'])
def testSLI():
    url = request.form['userUrl']
    successSLO = request.form['userSLOSuccess']
    speedSLO = request.form['userSLOSpeed']
    with open("results.txt", "w") as testSLIResults:
        testSLIResults.write("Here are the results for {}".format(url))
    speedSLOMet = 0
    successSLOMet = 0
    iterations = 0
    while(True):
        testIteration = requests.get(url)
        speedSLI = testIteration.elapsed.total_seconds()
        successSLI = testIteration.status_code
        if float(speedSLI) <= 0.1:
            speedSLOMet += 1
        if int(successSLI) > 199:
            if int(successSLI) < 500:
                successSLOMet += 1

        iterations += 1

        successPercentage = float(successSLOMet)/float(iterations) * 100 #always returns 100%
        speedPercentage = float(speedSLOMet)/float(iterations) * 100

        if float(successPercentage) >= float(successSLO):
            successFeedback = 'SLO OK!'
        else:
            successFeedback = 'SLO NOT OK!'

        if float(speedPercentage) >= float(speedSLO):
            speedFeedback = 'SLO OK!'
        else:
            speedFeedback = 'SLO NOT OK!'

        ########DEBUG BLOCK
        #print(str(successPercentage) + ', ' + str(successSLOMet) + ', ' + str(iterations))
        #comparasucesso = int(successPercentage) > int(successSLO)
        #comparavelocidade = int(speedPercentage) > int(speedSLO)
        #print(str(comparasucesso) + ', ' + str(comparavelocidade) + ' Success SLO:' + str(successSLO) + ' Speed SLO: ' + str(speedSLO) + ' Success SLI:' + str(successPercentage) + ' SpeedSLI:' + str(speedPercentage)
        #print(str(speedSLOMet) + '/ porcentagem ' + str(speedPercentage))
        #######END OF DEBUG BLOCK
        print ('N: '+ str(iterations) + ' ' + url + ' Status:' + str(successSLI) +', Successful requests SLI:' + str(successPercentage) +'% ('+ successFeedback + ')' + '. Response time:' + str(speedSLI) +'sec, Responses in less than 100ms SLI:' + str(speedPercentage) + '% (' + speedFeedback + ')')
        testSLIResults = open("results.txt", "a")
        testSLIResults.write('\n N: '+ str(iterations) + ' ' + url + ' Status:' + str(successSLI) +', Successful requests SLI:' + str(successPercentage) +'% ('+ successFeedback + ')' + '. Response time:' + str(speedSLI) +'sec, Responses in less than 100ms SLI:' + str(speedPercentage) + '% (' + speedFeedback + ')')
        testSLIResults.close()
        time.sleep(5)
if __name__ == '__main__': #The script that is going to be executed
    app.run(debug = True) #This facilitates development since you don't have to restart everything for every time you change your app, similar to nodejs
