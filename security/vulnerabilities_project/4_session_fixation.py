from flask import Flask, session, request, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'CHANGEME'

# A login form and session data is a common mechanism
# to authenticate users on a web application.
#
# The following route checks first that the 
# user is logged in (using the session) before displaying the page.
@app.route('/protected_page')
def protected_page():
    if 'logged_in' not in session:
        session['logged_in'] = False

    if session['logged_in']:
        return '<h1>You are logged in! You can see this page</h1>'
    else:
        return '<h1>Access Denied</h1>', 403

# Submit the following login form with credentials 'admin' and 'admin'.
# Now check your browser cookies
# (on Chrome: https://developer.chrome.com/docs/devtools/application/cookies/#open)
# What do you notice?
@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            session['logged_in'] = True
            return redirect('/protected_page')
        else:
            return "Invalid credentials!"
    else:
        return """
        <form action="/" method="post">
            <input type="text" name="username" />
            <input type="password" name="password" />
            <input type="submit" />
        </form>
        """

# Cookies-based session authentication stores
# the session information on a "cookie" (a small piece of data)
# on the user's device. The browser uses this cookie to 
# re-authenticate whenever it sends another request to the same server.
#
# A lot of web frameworks (like Flask) do encrypt cookies,
# however the safety of that encryption depends on a "secret key"
# set in the application configuration by the developers.
# If this key is easy to guess, or worse, the default one,
# it becomes _really_ easy for an attacker to "forge" a new session
# cookie and impersonate another user (maybe an admin?).
# This is called session fixation and is described in more details
# here: https://owasp.org/www-community/attacks/Session_fixation
# or here: https://martinfowler.com/articles/session-secret.html 
#
# To prevent this, developers need to ensure the secret key
# is set to a complex, hard to guess phrase. Such as
# 'U!p(ax3]Bag,WB!@io`RWeRE?zx$=,'

if __name__ == '__main__':
    app.run()