from  flask  import Flask,render_template,request,url_for,redirect,flash

app = Flask(__name__)

@app.route("/")
def  index():
  return  render_template("home.html")

@app.route("/signup.html")
def  hello():
  return  render_template("signup.html")

@app.route("/login.html")
def  signup():
  return  render_template("login.html")  

@app.route("/about.html")
def  profile():
  return  render_template("about.html")


@app.errorhandler(404)
def  page_not_found(error):  
  return  render_template('page_not_found.html'),404

if __name__=='__main__':
   app.run(debug=True)


   
