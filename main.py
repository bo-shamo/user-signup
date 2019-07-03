from flask import Flask, request, render_template

app=Flask(__name__)

app.config['DEBUG'] = True


@app.route('/')
def login():
    return render_template('index.html')

app.run()