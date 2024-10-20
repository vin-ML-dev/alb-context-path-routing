from flask import Flask

app1 = Flask(__name__)

@app1.route('/app2')
def welcome_app1():
    return "Welcome to app2"

@app1.route('/app2/check-health')
def health_check():
    # You can return a simple plain text or HTML response indicating the service is healthy.
    return "Health check passed", 200

if __name__ == '__main__':
    app1.run(host="0.0.0.0",port=5002)
