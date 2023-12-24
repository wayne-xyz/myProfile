from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html", name="Wayne J.")
    


if __name__=="__main__":
    app.run(debug=True,port=8000)


def check_email():
    return True

def check_url():
    return True

def check_jsonfile():
    return True