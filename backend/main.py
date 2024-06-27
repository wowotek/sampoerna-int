from flask import Flask

app = Flask(__name__)

@app.get("/")
def landing_page():
    ...

@app.post("/quotes")
def add_quotes():
    saved_quotes = []
    with open("quotes.txt", "r") as f:
        saved_quotes = f.readlines()

    saved_quotes.append("This is a new quote\n")
    
    with open("quotes.txt", "w") as f:
        for i in saved_quotes:
            f.write(i)
        
    with open("index.txt", "w") as f:
        f.write(str(len(saved_quotes)))

    return {"message": "success"}