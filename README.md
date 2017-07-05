# SRE-HandsOn
This program does a GET request for a given URL each 5 seconds, calculates the current SLI and compares to the given SLOs. Then it prints the details in the console and also prints the results in a text file.

It was used to the making of this project the following languages: HTML for frontend, Python and Flask for backend.

Flask is a microframework for Python based on Werkzeug. Great for simple projects and easy to setup.

Instructions:

1. How to setup: (For windows)

a. Firstly download this project
b. Install python Python 2.7.13 (not guaranteed working on 3.x.x versions) https://www.python.org/
c. Install pip https://pip.pypa.io/en/stable/installing/
d. Install flask with the command: pip install Flask - more details on http://flask.pocoo.org/

2. How to run:

a. Open the project folder in prompt of command or console if using Linux
b. Type set FLASK_APP=main.py or set FLASK_APP=main.py
c. Type Flask run
d. Open localhost:5000

3. How to use

a. Type the URL that you want to test (please don't forget the http://)
b. Type the SLO for HTTP status between 200 and 499 in %
c. Type the SLO for responses in less than 100ms in %
d. Press Submit
e. Results will apear in cmd or console and also will be written in results.txt in the project folder

Limitations: The limitations of this program are:

1. Does not test multiple URLs per instance (but you can open multiple instances with different URLs).
2. Does not show the results in a web app.
3. Does not have input validation

If i had more time, i'd add the following features:

1. Better input validation
2. Security measures
3. A propper front using Jquery and Bootstrap
4. Better presentation of data
5. The ability to test multiple URLs per instance
