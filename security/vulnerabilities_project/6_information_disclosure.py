from flask import Flask, session, request
import datetime

app = Flask(__name__)

# Information disclosure, also known as information leakage,
# is when an application unintentionally reveals sensitive information to users.
#
# A potential attacker could use this information to know very useful
# things for them, such as the technology you're using, it's version,
# any dependencies, and any other kind of details they could use
# to plan a more specific attack. In the worst case, your application
# could also accidentally leak sensitive data.
#
# This application works normally - but will break if the user
# enters anything other than a number in the text input.
# For example, if you type "roi", then submit, you will
# see a detailed error from Flask, as the 'debug' mode of Flask
# is enabled. An attacker could analyse this error,
# then try to exploit other vulnerabilities thanks to it.

@app.route('/')
def index():
    return '''<form method="POST" action="/submit">
        Enter your age: 
        <input type="text" name="age" />
        <input type="submit" />
    </form>'''

@app.route('/submit', methods=['POST'])
def submit():
    age = int(request.form.get('age'))
    current_year = datetime.date.today().year
    birth_year = current_year - age
    return '<h1>You are born in ' + str(birth_year) + '!</h1>'

if __name__ == '__main__':
    app.run(debug=True)