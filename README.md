# SRE-HandsOn
This program does a GET request for a given URL each 5 seconds, calculates the current SLI and compares to the given SLOs. Then it prints the details in the console and also prints the results in a text file.

It was used to the making of this project the following languages: HTML for frontend, Python and Flask for backend.

Flask is a microframework for Python based on Werkzeug. Great for simple projects and easy to setup.

Instructions:

How to setup: (For windows)

1. Firstly download this project
1. Install python Python 2.7.13 (not guaranteed working on 3.x.x versions) https://www.python.org/
1. Install pip https://pip.pypa.io/en/stable/installing/
1. Install flask with the command: pip install Flask - more details on http://flask.pocoo.org/

How to run:

1. Open the project folder in prompt of command or console if using Linux
1. Type set FLASK_APP=main.py or set FLASK_APP=main.py
1. Type Flask run
1. Open localhost:5000

How to use

3. Type the URL that you want to test (please don't forget the http://)
3. Type the SLO for HTTP status between 200 and 499 in %
3. Type the SLO for responses in less than 100ms in %
3. Press Submit
3. Results will apear in cmd or console and also will be written in results.txt in the project folder
3. To interrupt press Ctrl+C

Limitations: The limitations of this program are:

1. Does not test multiple URLs per instance (but you can open multiple instances with different URLs).
2. Does not show the results in a web app.
3. Does not have input validation
4. Does not have propper interruption mechanic

If i had more time, i'd add the following features:

1. Better input validation
2. Security measures
3. A propper front using Jquery and Bootstrap
4. Better presentation of data
5. The ability to test multiple URLs per instance
6. Propper interruption

#How the app works:

Flask is used to generate a server, this server renders the main page of the app, after the user input the information is sent back to the server. After getting the user input the server uses the given url to make a HTTP GET request using the python's request library and the response is stored in a object. This object has all the metadata needed to continue with the program. From the request is taken the status given from the URL and the time to answer the request, then those results are compared with the desired SLOs. Every time that the requests meets the goals given from the enunciate, its counted towards the respective variable. Then each iteration its compared wether the given from the user SLOs are being met and those informations are used to print in the console and also in a text flie the needed information.

NOTES:
- It was difficult to get a URL that returns a variable amount of statuses, mostly i got 200. But it used to test the http://httpstat.us/ and also http://amazon.com.br/ gave better results for debug.

- I didn't found a website that returned the requests in less than 100ms. For debugging purposes i increased the response time to aprox. 500ms and used sites that were inconstat for example: http://jovemnerd.com.br/

- Time was a decisive factor in the making of this project, finals season are on their way in college so the program being simple but functional makes me proud.
