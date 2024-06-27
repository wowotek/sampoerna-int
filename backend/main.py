from flask import Flask
from flask import request
from flask import send_from_directory
from flask import render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.get("/")
@cross_origin()
def landing_page():
    return render_template("index.html")

@app.route("/quotes", methods=['POST'])
@cross_origin()
def add_quotes():
    saved_quotes = []
    with open("quotes.txt", "r") as f:
        saved_quotes = f.readlines()

    new_quote = str(request.json['quote'])
    saved_quotes.append(new_quote + "\n")
    
    with open("quotes.txt", "w") as f:
        for i in saved_quotes:
            f.write(i)
        
    with open("index.txt", "w") as f:
        f.write(str(len(saved_quotes)))
    
    with open("currentQuotes.txt", "w") as f:
        f.write(new_quote)

    return {"message": "success"}