from flask import Flask, render_template, request, make_response
app = Flask(__name__)
@app.route('/')
def index():
    return "/hello"
@app.route('/hello', methods=['GET', 'POST', 'DELETE'])
def hello():
    if 'pita' in request.cookies and request.cookies['pita'] == 'wrap':
        if request.headers['User-Agent'] == 'shrek':
            res = make_response()
            res.set_cookie("c00kie", value="flag{shr3k_n33ds_h3lp_3at1ng_p1t4}")
            return res
        else:
            return "set user agent header to shrek"
    return "make a cookie called pita and set it to value wrap"
