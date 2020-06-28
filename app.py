from gevent import monkey
monkey.patch_all()

from app import app
from app.movies.views import movies
from flask_socketio import SocketIO
from app.config.socket import SocketConfig

app.register_blueprint(movies)

socketio = SocketIO(app, **SocketConfig)

if __name__ == '__main__':
    socketio.run(app, host="localhost", port=8000)