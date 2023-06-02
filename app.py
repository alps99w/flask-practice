from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello from the earth!'

@app.route('/upload', methods=['POST'])
def upload_file():
    return "This is a post method"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)

