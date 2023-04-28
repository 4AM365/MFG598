#William Craig
#MFG 598
#April 27, 2023
#Week 15 Practice w/ Flask

from flask import Flask, request, jsonify
import pandas as pd
import os

#Had to path join so this could load.
csv_file = os.path.join(os.path.dirname(__file__), "5000 Sales Records.csv")
df = pd.read_csv(csv_file)

app = Flask ("My App")


@app.route("/")

def homemsg():
    return "Hello! This is my homepage."

@app.route("/totalrecords")
def getNoRecords():
    total = len(df.index)
    return f"Total Records = {total}"

#https://localhost:3500/data/filter?region=Asia&country=India

@app.route("/data/filter")
def filterR():
    #Need to read about why we need this.
    region = request.args.get('region')
    country = request.args.get('country')
    newdf = df[(df["Region"]==region)*(df["Country"]==country)]
    total = len(newdf.index)
    return f"Total Records:{total}"


@app.route("/getalldata")
def getalldata():
    # return str(df)
    return jsonify(df.to_json(orient='records'))

if __name__ == "__main__":
    app.run(host = "localhost", port = 3500, debug=True)