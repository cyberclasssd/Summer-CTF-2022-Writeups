import base64
from flask import Flask, render_template, request, send_file

app = Flask(__name__)


@app.route("/")
def nothing_to_see_here():
    return "<h1>Nothing to see here! We totally don't have a secret bingo facility or anything.</h1>"


@app.route("/flag")
def flag():
    if "grandma" in request.cookies and check_cookie(request.cookies.get("grandma")):
        return send_file("./flag.txt")
    else:
        return "<h1>You are an IMPOSTER grandma!</h1>\n<h2>GET OUT OF OUR BINGO RESEARCH FACILITY CENTER NOW OR ELSE. </h2>"


def check_cookie(encrypted_cookie):
    decrypted_cookie = base64.b64decode(encrypted_cookie[::2]).decode("ascii")
    return decrypted_cookie == "1_4m_a_l337_6r4ndm4_wh0_l1k35_c00k135"


if __name__ == "__main__":
    app.run()
