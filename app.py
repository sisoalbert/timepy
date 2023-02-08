from flask import Flask, make_response
from datetime import datetime

app = Flask(__name__)

@app.route("/time")
def get_current_time():
    current_time = str(datetime.now().time())
    response = make_response(current_time)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run()
