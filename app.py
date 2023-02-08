from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/time")
def get_current_time():
    current_time = str(datetime.now().time())
    return current_time

if __name__ == '__main__':
    app.run()
