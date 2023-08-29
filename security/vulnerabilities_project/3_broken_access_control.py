from flask import Flask, session, request, escape

app = Flask(__name__)

# (We used a global variable here to simplify things,
# in a real application we would likely have a database.)
users_list = []

# Most deployed applications use some kind of database to store data. Often this
# data contains what is called PII, or Personal identifiable information. This
# is any data related to an individual, like a name, an email address, social
# security number, etc.

@app.route('/')
def index():
    return '''<form method="POST" action="/submit">
        <input type="text" name="first_name" />
        <input type="text" name="last_name" />
        <input type="text" name="email" />
        <input type="submit" />
    </form>'''

@app.route('/submit', methods=['POST'])
def submit():
    global users_list
    users_list.append(request.form.to_dict())
    
    return 'Thanks for registering! Go see <a href="/people">users list</a>'

# In most cases, this data shouldn't be read or accessed by anone outside of the individual.
# If it's in a database, you'll need to ensure the database cannot be accessed by anyone
# outside your organisation.
# It also means that this information cannot be accessed by other users
# through your web application.

@app.route('/people')
def people_list():
    global users_list
    resp = ""
    for user in users_list:
        resp += f"{user['first_name']} {user['last_name']} {user['email']}"
        resp += "<br/>"
    return resp

if __name__ == '__main__':
    app.run()