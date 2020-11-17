from application import app

_port = 3000
_debug = True
_host = '0.0.0.0'

if __name__ == "__main__":
    app.run(host=_host, port=_port, debug=_debug)
