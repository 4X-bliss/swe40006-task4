from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>SWE40006 Task 4.2</h1>
    <p>Hello from my Python Flask application!</p>
    <p>This application is running inside a Docker container.</p>
    """


@app.route("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)