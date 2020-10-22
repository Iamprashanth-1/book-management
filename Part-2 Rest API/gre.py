import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import backend

app=Flask(__name__)
@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/view",methods=["POST"])
def view():
    ph=[]
    for row in backend.view():
       # print(row)
        ph.append(row)
    return render_template('results.html',result=ph)
@app.route("/insert",methods=["GET","POST"])
def insert():
    if request.method == "POST":
        req = request.form
        l=['NULL']*5
        c=0
        for key,value in req.items():
           l[c]=value
           c+=1
        backend.insert(l[0],l[1],l[2],l[3])
    
    return render_template("home.html")

@app.route("/selecte",methods=["GET","POST"])
def selecte():
    if request.method =="POST":
        reqs=request.form
        s=[]
       # print(reqs)
        for key,value in reqs.items():
            s.append(value)
            print(s)
        te=backend.selected(s[0])
        #print(te,'po')
    return render_template('home.html',booki=te)


@app.route('/updat',methods=["GET","POST"])
def updat():
    if request.method=="POST":
        re=request.form
        l=[]
        for key,value in re.items():
           l.append(value)
       # print(re)
        backend.update(l[1],l[2],l[3],l[4],l[0])
    return render_template('home.html')
@app.route("/delet",methods=["GET","POST"])
def delet():
    if request.method == "POST":
        reqs = request.form
        s=[]
        print(reqs)
        for key,value in reqs.items():
            s.append(value)
           # print(s)

        backend.delete(s[0])
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)