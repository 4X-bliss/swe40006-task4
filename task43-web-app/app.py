from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

APP_MESSAGE = os.getenv(
    "APP_MESSAGE",
    "Environment variable not configured"
)

APP_ENV = os.getenv(
    "APP_ENV",
    "development"
)


@app.route("/")
def home():
    hostname = socket.gethostname()

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>SWE40006 Task 4.3</title>

        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 60px auto;
                padding: 20px;
                background: #f4f6f8;
            }}

            .card {{
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.10);
            }}

            code {{
                background: #eeeeee;
                padding: 3px 6px;
            }}
        </style>
    </head>

    <body>
        <div class="card">
            <h1>SWE40006 Task 4.3</h1>

            <h2>Container Deployment Dashboard</h2>

            <p>
                This custom Flask application is running
                inside a Docker container.
            </p>

            <p>
                <strong>Environment:</strong>
                {APP_ENV}
            </p>

            <p>
                <strong>Environment Message:</strong>
                {APP_MESSAGE}
            </p>

            <p>
                <strong>Container Hostname:</strong>
                <code>{hostname}</code>
            </p>

            <p>
                <strong>Health Endpoint:</strong>
                <a href="/health">/health</a>
            </p>
        </div>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify(
        status="healthy",
        environment=APP_ENV,
        service="swe40006-task43"
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000
    )