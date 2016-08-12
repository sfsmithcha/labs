from flask import Flask, render_template
import os
import random
import socket

app = Flask(__name__)

container_hostname = socket.gethostname()

# list of Docker images
images = [
"./static/docker-turtles-communication.png",
"./static/island-docker.png",
"./static/project1.png",
"./static/project2.png",
"./static/team-12.png",
"./static/team-2.png",
"./static/team-3.png",
"./static/team-7.png",
"./static/team-9.png",
"./static/underwater-docker.png",
"./static/underwater-docker.png"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url, hostname=container_hostname)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
