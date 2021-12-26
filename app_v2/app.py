from flask import request, Flask
import socket

app = Flask(__name__)

@app.route('/')
def helloV2():
    ip = socket.gethostbyname(socket.gethostname())
    return f'Hello V2 - {ip}', 2

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')