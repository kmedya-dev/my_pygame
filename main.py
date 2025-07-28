from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, Flask!</h1><p>This is a simple web page.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)