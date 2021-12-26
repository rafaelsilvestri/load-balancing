from flask import request, Flask
import socket

app = Flask(__name__)

@app.route('/')
def helloV1():
    ip = socket.gethostbyname(socket.gethostname())
    return f'Hello V1 - {ip}', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')