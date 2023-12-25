from flask import Flask,render_template
import re
import json


app=Flask(__name__)

#checking the personal email is valid
def check_email(email):
    # Define the regular expression pattern for a valid email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    # Use re.match to check if the email matches the pattern
    match = re.match(pattern, email)
    print(f"Is email valid:{bool(match)}")
    # If there is a match, the email is valid; otherwise, it's not
    return bool(match)

#checking the url from json file with the keylist
def check_url(json_data,key_list):
    try:
        urls=[]
        # Recursive function to traverse the JSON data
        def traverse(obj):
            if isinstance(obj, list):
                for item in obj:
                    traverse(item)
            elif isinstance(obj, dict):
                for key, value in obj.items():
                    if key in key_list:urls.append(value)
                    elif isinstance(value, (list, dict)):
                        traverse(value)
        # run the recursive function findout all the urls
        traverse(json_data)
        for url in urls: 
            url_pattern = re.compile(r'^https?://\S+$', re.IGNORECASE)
            if bool(url_pattern.match(url))==False: # validate all the urls
               return False
        return True
    except Exception as e:
        # An exception may be raised for malformed URLs
        print(f"Error checking URL validity: {e}")
        return False
    
#checking keys in json file should same as the template
def check_jsonfile(json_data):
    try:
        with open("example.json","r") as example_file:
            example_data=json.load(example_file)
            return set(example_data.keys())==set(json_data.keys())# return t is the keys is same 
    except (FileNotFoundError, json.JSONDecodeError):
        # Handle file not found or invalid JSON file
        return False    
    
#main function to render the main page of the profile website
@app.route("/")
def main():
    try:
        with open("person.json","r") as file:
            jsondata= json.load(file)
            if check_jsonfile(jsondata) and check_email(jsondata["contact"]["email"]) and check_url(jsondata,["linkedin","github","url"]):
                print("json file valided")
                return render_template("index.html", data=jsondata)
            else:
                print("something wrong with your json file")
                return four_o_four()
    except :
        print ("Something erro")
        return four_o_four()
        
    
@app.route("/404")
def four_o_four():
    return render_template("404.html")

if __name__=="__main__":
    app.run(debug=True,port=8000)


