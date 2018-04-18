from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return ('<html><header><title>This is title</title></header>'
            '<body>Hello world</body></html>')
@app.route('/get')
def replicate():
    user_text = request.args.get('msg')
    return user_text.upper()

if __name__ == "__main__":
    app.run()