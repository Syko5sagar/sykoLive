from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/boost', methods=['POST'])
def boost():
    url = request.form.get('url')
    boost_type = request.form.get('type')
    return f"Boosting {boost_type} for: {url}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
