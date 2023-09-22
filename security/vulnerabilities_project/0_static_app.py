from flask import Flask, session

app = Flask(__name__)

# An application which doesn't do much 
# often has _almost_ no security vulnerability.
#
# You can run this app by running in your terminal:
# python3 0_static_app.py
# 
# Now move on to 1_injections.py

@app.route('/')
def index():
    return '<h1>Welcome</h1>'

if __name__ == '__main__':
    app.run()