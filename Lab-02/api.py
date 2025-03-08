from flask import Flask, request, jsonify
crom cipher.caesar import CaesarCipher
app = Flask(__name__)

#CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", method=["POST"])
def caesar_cipher():
    data = request.json
    plain_text = data['plain_text']
    key = int (data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})