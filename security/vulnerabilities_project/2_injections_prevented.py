from flask import Flask, session, request, escape

app = Flask(__name__)

# You've just used something called an "injection".
#
# Whenever users can submit data to your application, there's a potential
# for them to "inject" malicious code. In this specific case, this code was
# some JavaScript. This is called XSS (Cross Site Scripting) injection.
# The browser reads the JS code and executes it.

# In this case we've only showed an alert to the user. Annoying, but pretty
# inoffensive. However, other JS code could be used to redirect the user to a
# different website, run code without them noticing, save cookies in their
# browser, or other things. This could lead to bigger problems.

# In the code below, we've fixed this by escaping the user-submitted input,
# before displaying it in the browser. Generally, any kind of user input can be
# considered "tainted", and potentially harmful — it should always be validated
# and sanitised in some way.

# Run this file and try to inject JavaScript code like done previously.
# What's different?

@app.route('/')
def index():
    return '''<form method="POST" action="/submit">
        <input type="text" name="message" />
        <input type="submit" />
    </form>'''

@app.route('/submit', methods=['POST'])
def submit():
    return '<h1>You submitted: ' + escape(request.form['message']) + '</h1>'

if __name__ == '__main__':
    app.run()