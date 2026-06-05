from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "name": "Football AI",
        "status": "running",
        "version": "1.0",
        "sources": [
            "BBC Football",
            "ESPN FC",
            "Yahoo Soccer",
            "Goal.com",
            "90min"
        ]
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
