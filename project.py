from flask import Flask,render_template
import re
import json
from urllib.parse import urlparse


app=Flask(__name__)

#function that can check the personal email is valid
def check_email(email):
    # Define the regular expression pattern for a valid email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # Use re.match to check if the email matches the pattern
    match = re.match(pattern, email)
    print(f"Is email valid:{bool(match)}")
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
    

# this function for checking keys in json file 
def check_jsonfile(json_data):
    try:
        with open("example.json","r") as example_file:
            example_data=json.load(example_file)
            return set(example_data.keys())==set(json_data.keys())# return t is the keys is same 
    except (FileNotFoundError, json.JSONDecodeError):
        # Handle file not found or invalid JSON file
        return False    
    

@app.route("/")
def main():
    try:
        with open("person.json","r") as file:
            jsondata= json.load(file)
            if check_jsonfile(jsondata) and check_email(jsondata["contact"]["email"]):
                print("json file valided")
            else:
                print("something wrong with your json file")
        return render_template("index.html", name="Wayne J.")
    except (FileNotFoundError, json.JSONDecodeError):
        print ("Json erro")
    
@app.route("/404")
def four_o_four():
    return render_template("404.html")

if __name__=="__main__":
    app.run(debug=True,port=8000)


