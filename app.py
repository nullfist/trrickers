from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/")
def index():
    role = request.cookies.get("role", "user")

    if role == "admin":
        return "Admin Panel<br><br>FLAG: NULLCTF{cookies_should_not_decide_roles}"

    resp = make_response("Hello user. Nothing interesting here.")
    resp.set_cookie("role", "user")
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
