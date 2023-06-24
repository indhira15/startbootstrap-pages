from flask import Flask, flash, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"

@app.route('/')
def inicio():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=3000, host="0.0.0.0",debug=True)