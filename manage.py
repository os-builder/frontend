#!/bin/env python3
from flask_script import Server, Manager
app = __import__('src-py').app


manager = Manager(app)

server = Server(host="0.0.0.0", port=8000)
manager.add_command("runserver", server)

manager.run()

