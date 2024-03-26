import os
import csv

from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return send_file('index.html')

# create a route named as write2csv that only works on post method
@app.route("/write2csv", methods=["POST"])
def write2csv():
    # get the data from the request which was passed as params
    data = request.get_json()
    # store all the data into the Audit.csv file
    with open('Audit.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    return "success"


def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
