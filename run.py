from flask import Flask, render_template,request,make_response,abort,flash
from datetime import datetime
from werkzeug.utils import secure_filename                                #to get secure file name

app = Flask(__name__,template_folder="templates")                   #see templates folder for html pages

app.secret_key="mysecretkey"                               
@app.route("/")                                                     #render this for empty routes
def home():
    return render_template("index.html")
    
@app.route("/about")                                                #about route
def about():
    current_time=datetime.now()
    return render_template("about.html", current_time=current_time)

@app.route("/form",methods=["POST","GET"])                           #route accepts data only from GET method here POST is explicitly accepted
def form():
    error=None
    if request.method =="POST":                                      #for POST requests(when user submits the form a post requst is sent with form data)
        print(request.form )                                         #request.form get data from form if form uses post or put method
                                                                     #if form uses get method then request.args should be used
        name=request.form ["name"]
        email=request.form ["email"]
        print(name,email)                                            #output to terminal
        print(f"Name: {name}, Email: {email}")
        f=request.files["file"]                                      #get form data
        f.save(secure_filename(f.filename))                          #ensures the file name is secure and save it
        if request.form["name"] == "sava" and request.form["email"] == "savandikodithuwakku@gmail.com":
            flash("User logged in successfully")
            return render_template("show.html", name=name, mail=email) 
        else:
            # abort(401)                                             #UNauthorized error msg 
            error="Invalid username or password"
    #else:
    return render_template("form.html",error=error)                  #for GET requests(from index.html it directs to form.html)

@app.route('/set')
def set():
    return render_template('setcookie.html')

@app.route('/setcookie',methods=['POST','GET'])                      #setting the cookie
def setcookie():
    if request.method=='POST':
        user=request.form['nm']
        resp=make_response(render_template('readcookie.html'))       #resp is a response object. It creates a response object from the readcookie page    
        resp.set_cookie('userID',user)                               #add cookie details as a response header which instruct the user to save the cookie
        return resp                             #return resp(setcookie header+readcookie page) to save the cookie in browser and return to readcookie page

@app.route('/getcookie')                                             #getting the cookie
def getcookie():    
    name=request.cookies.get('userID')                               #request.cookies.get('userID') returns the value of userID
    return '<h1>welcome '+name+'</h1>'

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)                 #run the app by starting the server
