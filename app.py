# app.py
from flask import Flask, render_template, request
from utils.analyze_url import analyze_url

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        url = request.form.get('url')  # Get the URL entered by the user
        result = analyze_url(url)  # Call the analyze_url function to check if it's phishing or legitimate
    return render_template('index.html', result=result)  # Render the result on the index.html page

if __name__ == '__main__':
    app.run(debug=True)
