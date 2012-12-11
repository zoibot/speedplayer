import os
import urllib2
import xml.etree.ElementTree as ET

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html') 

@app.route('/play/<path:feed_url>')
def play(feed_url=''):
    headers = { 'User-Agent' : 'Mozilla/5.0' }
    req = urllib2.Request(feed_url, None, headers)
    resp = urllib2.urlopen(req)
    root = ET.fromstring(resp.read())[0]
    metadata = {}
    items = []
    for elem in root:
        if elem.tag == 'item':
            items.append(elem)
        elif 'itunes' not in elem.tag:
            metadata[elem.tag] = elem.text
    return render_template('play.html', feed_url = feed_url, metadata = metadata, items = items)

if __name__ == '__main__':
    app.debug = True
    app.run()
