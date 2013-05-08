from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Add noun to URL:<ul><li>fuckyeah/{noun}</li></ul>"

@app.route('/fuckyeah/<noun>')
def fuckyeah(noun):
    google_search_url = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&rsz=8&q=%s" % noun
    r = requests.get(google_search_url)
    if r.status_code == 200:
        response = json.loads(r.content)
        image_url = response['responseData']['results'][0]['unescapedUrl']
        return "<p align='center'><img src='%s' width=400 height=400></p>" % image_url
    else:
        return "%s" % r.content

if __name__ == "__main__":
    app.run()
