from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello from Jenkins CI/CD!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
