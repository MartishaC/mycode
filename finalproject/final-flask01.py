#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from flask import render_template

import json

app= Flask(__name__)

@app.route("/<statename>")
def index(statename):
    return render_template("state.html", name = statename)

statedata= [{
    "stateName": "Texas",
    "governor": "Greg Abbott",
    "since": 1845,
    "randomFacts": [
        "bluebonnet flower",
        "northern mockingbird",
        "friendship motto",
        "lone star state"
              ]
             }]

@app.route("/", methods=["GET","POST"])
def valid():
    if request.method == 'POST':
        data = request.json
        if data:
           data= json.loads(data)
           stateName = data["stateName"]
           governor = data["governor"]
           since = data["since"]
           randomFacts = data["randomFacts"]
           statedata.append({"stateName":stateName,"governor":governor,"since":since,"randomFacts":randomFacts})

    return jsonify(statedata)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

