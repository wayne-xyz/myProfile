from flask import Flask,render_template
import re
from urllib.parse import urlparse

app=Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html", name="Wayne J.")
    


if __name__=="__main__":
    app.run(debug=True,port=8000)


#function that can check the personal email is valid
def check_email(email):
    # Define the regular expression pattern for a valid email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Use re.match to check if the email matches the pattern
    match = re.match(pattern, email)

    # If there is a match, the email is valid; otherwise, it's not
    return bool(match)

#function that can check the url
def check_url(url):
    try:
        # Parse the URL
        parsed_url = urlparse(url)

        # Check if the scheme (protocol) is present and either "http" or "https"
        if parsed_url.scheme and parsed_url.scheme in ('http', 'https'):
            return True
        else:
            return False
    except Exception as e:
        # An exception may be raised for malformed URLs
        print(f"Error checking URL validity: {e}")
        return False
    

def check_jsonfile():
    return True