from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return'<html><h1>HOME PAGE</h1><p>Welcome here!!</p><a href=\'/food\'><go to the first food photo/a></html>'




@app.route('/food')
def food():
    return'<html>


if __name__ == '__main__':
    app.run(debug=True)