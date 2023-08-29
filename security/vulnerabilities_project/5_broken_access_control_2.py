from flask import Flask, session, request, escape

app = Flask(__name__)

# We used a global variable here to simplify things,
# in a real application we would likely have a database.
users_list = [
    { 'id': 12, 'name': 'Alice' },
    { 'id': 13, 'name': 'Beatriz' },
    { 'id': 14, 'name': 'Carol' },
]

# That's another example of broken access control.
# Looking at the URL pattern, an attacker can quickly guess
# they could just replace their own user ID with any other ID
# and try to access another user's profile. They could automate
# this, and quickly check thousands of different URLs.
#
# If access to other users profiles is not controlled in some way,
# this attacker could, at best, "scrap" (record) all of your users data
# from their profile page, or, at worst, access and record private information
# about them (they could publish it online, sell it,
# use it to blackmail the organisation, etc.)
# 
# Some ways to prevent this:
#
#  - Best to use non-numerical IDs which cannot be easily guessed in sequence
#    (for example, '/users/a656e9787e0f')
#  - If a URL can be used to access private information, it shouldn't be publicly accessible.
#    Don't assume people won't "guess" or find the URL to access it!

@app.route('/users/<int:id>')
def show_user(id):
    # This finds user info by their ID.
    user = list(filter(
        lambda user: (user['id'] == id),
        users_list
    ))

    return str(user[0])

if __name__ == '__main__':
    app.run()