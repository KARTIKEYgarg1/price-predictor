from flask import Flask,render_template,request
from utils import PredictTheValue
app=Flask(__name__)
@app.route("/",methods=["POST","GET"])
def home():
    if request.method=="GET":
        return render_template("index.html")
    else:
        print("calculating")
        ar=int(request.form["area"])
        bd=int(request.form["bedr"])
        ag=int(request.form["age"])
        pred=PredictTheValue(ar,bd,ag)
        pred=" Approximate Price:- Rs."+str(pred)
        print(pred,ar,bd,ag)
        return render_template("index.html",pred=pred,ar=ar,bd=bd,ag=ag)    
if __name__ == "__main__":
    app.run(debug=True)