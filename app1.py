from flask import Flask, request, session, render_template, url_for,
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('homepage.html')

    if __name__ == '__main__'
        app.run(debug=True)
