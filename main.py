#This program receives a string with a URL, the SLO for successful responses (double) and its the SLO for response time (double)
#Makes a HTTP GET request every 5 seconds and calculates the current SLIs.
#It displays for each URL the current SLIs, the SLOs and wheter the SLOs are being met

from flask import Flask, request, render_template #All Flask stuff

app = Flask(__name__)

@app.route('/sup') #DEBUG page, serves to see if basic server cfgs are working
def hello_world():
    return 'Hello inloco!'

@app.route('/') #Main page, will get the URL and the desired SLOs
def index():
    return render_template('index.html')

#This will render index.html for the user when localhost:5000/ is requested

if __name__ == '__main__': #The script that is going to be executed
    app.run(debug=True) #This facilitates development since you don't have to restart everything for every time you change your app, similar to nodejs
