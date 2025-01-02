from flask import Flask, render_template,request
from datetime import datetime

app = Flask(__name__,template_folder="templates") #see templates folder for html pages

@app.route("/") #render this for empty routes
def home():
    return render_template("index.html")
    
@app.route("/about") #about route
def about():
    current_time=datetime.now()
    return render_template("about.html", current_time=current_time)

@app.route("/form",methods=["POST","GET"])             #route accepts data only from GET method here POST is explicitly accepted
def form():
    if request.method =="POST":        #for POST requests(when user submits the form a post requst is sent with form data)
        data=request.form              #request.form get data from form if form uses post method
                                                            #if form uses get method then request.args should be used
        print(data)
        name=data["name"]
        email=data["email"]
        print(name,email)        #output to terminal
        print(f"Name: {name}, Email: {email}")
        return render_template("show.html", name=name, mail=email) 
    #else:
    return render_template("form.html")                #for GET requests(from index.html it directs to form.html)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)


