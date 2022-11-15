from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'b95359c2505145f16c6aaa384f9cc74eeff78eb36d308ca4fd902eeeb0a0b161b'

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
