from flask import Flask, session, request, redirect

# This web application contains a few different
# security vulnerabilities. Set a timer to thirty minutes
# maximum, and try to find as many as you can in that time.
#
# When you're done with it, check out the solution
# in the README.md file

from flask import Flask, request

app = Flask(__name__)

messages = []

@app.route('/')
def index():
    messages_html = ""
    for message in messages:
        messages_html += f"<p data-email={message['email']}>{message['username']}: {message['message']}</p>"
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Visitors book</title>
    </head>
    <body>
        <h2>Leave a message!</h2>
        <form action="/submit" method="get">
            Username:<br />
            <input type="text" id="username" name="username" required><br />
            Email (we promise this won't be shown to other people!):<br />
            <input type="text" id="email" name="email" required><br />
            Message:<br />
            <textarea id="message" name="message" required></textarea><br />
            <input type="submit" value="Submit">
        </form>
        <h2>All messages posted so far:</h2>
        {messages_html}
    </body>
    </html>
    """

@app.route('/submit', methods=['GET'])
def submit():
    global messages
    username = request.args.get('username')
    message = request.args.get('message')
    email = request.args.get('email')
    messages.append({'username': username, 'email': email, 'message': message})
    return """
    <h1>Message Submitted</h1>
    <a href="/">Back to form</a>
    """

# This route DELETEs all messages
# Web browsers cannot send requests with a DELETE HTTP method,
# so there's no risk someone will accidentally navigate to this URL.
@app.route('/messages', methods=['DELETE'])
def delete_messages():
    global messages
    messages = []
    return ""

if __name__ == '__main__':
    app.run(debug=True)