from re import S
import flask
from flask import Flask, request, Response
from dh import*

app = Flask(__name__)

s_public = 0

m_public = 197197
m_private = 199199

@app.route('/partial-key/<key>', methods=['POST'])
def make_partial_key(key):
    s_public = int(key)
    cl = DH_Endpoint(s_public, m_public, m_private)
    part_key = cl.generate_partial_key()

    return str(part_key)

@app.route('/full-key/<partKey>', methods=['POST'])
def make_full_key(pubKey, partKey):
    param_key = int(partKey)
    cl = DH_Endpoint(s_public, m_public, m_private)
    full_key = cl.generate_full_key(param_key)

    return str(full_key)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8091)