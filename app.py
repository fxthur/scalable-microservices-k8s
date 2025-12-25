from flask import Flask, request, make_response, render_template_string
import os
import random
import redis
import socket
import sys

app = Flask(__name__)

# --- KONFIGURASI PILIHAN (UBAH DISINI) ---
option_a = "PERSIB"
option_b = "PERSIJA"
# -----------------------------------------

hostname = socket.gethostname()

# Setup Redis Connection
redis_host = os.getenv('REDIS_HOST', 'localhost')
try:
    r = redis.Redis(host=redis_host, port=6379, db=0, socket_timeout=5)
except Exception as e:
    print(f"Error connecting to Redis: {e}")
    r = None

@app.route("/", methods=['GET', 'POST'])
def hello():
    voter_id = request.cookies.get('voter_id')
    if not voter_id:
        voter_id = hex(random.getrandbits(64))[2:-1]

    vote = None

    if request.method == 'POST':
        vote = request.form['vote']
        if r:
            data = JSON.dumps({'voter_id': voter_id, 'vote': vote})
            r.rpush('votes', data)
    
    # HTML Sederhana di dalam Python
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{option_a} vs {option_b}!</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {{ font-family: sans-serif; text-align: center; padding: 50px; color: #333; }}
            button {{ width: 300px; height: 100px; font-size: 24px; color: white; border: none; margin: 10px; cursor: pointer; border-radius: 5px; }}
            .a {{ background-color: #1E88E5; }} 
            .b {{ background-color: #00ACC1; }}
            .container {{ max-width: 700px; margin: auto; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h3>{option_a} vs {option_b}!</h3>
            <form method="POST">
                <button name="vote" value="a" class="a">{option_a}</button>
                <button name="vote" value="b" class="b">{option_b}</button>
            </form>
            <p><small>Processed by container ID: {hostname}</small></p>
        </div>
    </body>
    </html>
    """
    resp = make_response(html)
    resp.set_cookie('voter_id', voter_id)
    return resp

import json as JSON

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
