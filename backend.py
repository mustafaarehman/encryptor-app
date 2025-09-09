from flask import Flask, request, jsonify,render_template
import random, string

app = Flask(__name__)

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

def get_key(password):
    random.seed(password)
    key = chars.copy()
    random.shuffle(key)
    return key

@app.route("/")
def home():
    return render_template("index.html")   # 👈 serves your index.html

@app.route("/encrypt", methods=["POST"])
def encrypt():
    data = request.json
    password = data["password"]
    plain_text = data["message"]

    key = get_key(password)
    cipher_text = ""
    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

    return jsonify({"encrypted": cipher_text})

@app.route("/decrypt", methods=["POST"])
def decrypt():
    data = request.json
    password = data["password"]
    cipher_text = data["message"]

    key = get_key(password)
    plain_text = ""
    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]

    return jsonify({"decrypted": plain_text})

if __name__ == "__main__":
    app.run(debug=True)
