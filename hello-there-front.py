from flask import Flask, redirect, url_for, render_template
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    # Display a hello message and then redirect to /Lab-com
    return redirect(url_for('labcom'))


@app.route('/Lab-com')
def labcom():
    message = "Hello there"
    backend_val = get_value()
    message_full = message + " " + backend_val
    background_url = "/static/He-says-the-thing.webp"  # URL or relative path to your background image
    return render_template('labcom.html', message=message_full, background_url=background_url)


def get_value():
    response = requests.get('http://localhost:5001/api/get-value')
    if response.status_code == 200:
        return response.json()['value']
    else:
        return "Error fetching value"



if __name__ == '__main__':
    app.run(host='0.0.0.0')
