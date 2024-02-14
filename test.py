from flask import Flask, render_template

app=Flask("__name__")

@app.route("/")
def hello_world():
    #return "Hello you mother fucker!"
    return render_template("index.html")

@app.route("/main")
def main():
    Result=plus(2,3)
    return "you fuck ass hole "+str(Result)

def plus(a,b):
    return a+b

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)