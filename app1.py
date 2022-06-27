from flask import Flask

app=Flask(__name__)

@app.route("/",methods=['GET','POST']
def hello():
    if (request.method=="GET'):
        print("hello everyone")

if __name__="__main__":
    app.run(port=8000)

