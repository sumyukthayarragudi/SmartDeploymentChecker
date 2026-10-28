
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Smart Deployment Checker</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f5f8fc;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }
            .card {
                background: white;
                width: 90%;
                max-width: 750px;
                padding: 40px 20px;
                text-align: center;
                border-radius: 18px;
                box-shadow: 0 5px 25px #00000015;
                box-sizing: border-box;
            }
            .check {
                background: #55ca83;
                color: white;
                width: 110px;
                height: 110px;
                line-height: 110px;
                font-size: 70px;
                border-radius: 50%;
                margin: 0 auto 15px;
            }
            h1 {
                color: #10213a;
                font-size: clamp(25px, 5vw, 42px);
                margin: 15px 0 25px;
            }
            h2 {
                color: #20a464;
                font-size: clamp(22px, 4vw, 32px);
            }
            .status {
                display: inline-block;
                background: #0eaf69;
                color: white;
                padding: 15px 25px;
                border-radius: 30px;
                font-size: 20px;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <div class="check">&#10003;</div>
            <h1>Smart Deployment Checker</h1>
            <h2>Deployment Successful!</h2>
            <div class="status">Application Status: Healthy</div>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

