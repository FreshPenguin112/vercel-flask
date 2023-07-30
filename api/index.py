from flask import Flask
from brotlipy import compress, decompress

app = Flask(__name__)

@app.route('/c/<x>')
def home(x):
    return compress(x)

@app.route('/d/<x>')
def about(x):
    return decompress(x)
