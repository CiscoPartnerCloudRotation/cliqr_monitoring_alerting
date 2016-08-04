from flask import Flask
import json
app = Flask(__name__)

@app.route('/v1/jobs/1768')
def jobinfo():
    with open("sample_output/jobresult.json") as json_file:
        json_data = json.load(json_file)
    return str(json_data)

@app.route('/v1/jobs')
def joblist():
    with open("sample_output/joblist.json") as json_file:
        json_data = json.load(json_file)
    return str(json_data)

if __name__ == "__main__":
    app.run()